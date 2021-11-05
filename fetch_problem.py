"""
    USAGE:

    길게
    python3 fetch_problem.py --name "양영광" --week "week3" --problems 11725 1967 3584 ...

    단축 
    python3 fetch_problem.py -n "양영광" -w "week3" -p 11725 1967 3584 ...

    단축2
    python3 fetch_problem.py -n 양영광 -w week3 -p 문제번호1 문제번호2

"""

from collections import defaultdict
import json
import urllib.request
import argparse
import datetime
import html
import os

__template = """
\"\"\"
    문제 이름: <problem_name>
    문제 번호: <problem_id>
    문제 링크: <url>
    난이도: <difficulty>
    태그: <tags>
\"\"\"
import sys 

def input(): return sys.stdin.readline().rstrip()
"""

__tier_text = {
    0: "Unknown",
    1: "Bronze V",
    2: "Bronze IV",
    3: "Bronze III",
    4: "Bronze II",
    5: "Bronze I",
    6: "Silver V",
    7: "Silver IV",
    8: "Silver III",
    9: "Silver II",
    10: "Silver I",
    11: "Gold V",
    12: "Gold IV",
    13: "Gold III",
    14: "Gold II",
    15: "Gold I",
    16: "Platinum V",
    17: "Platinum IV",
    18: "Platinum III",
    19: "Platinum II",
    20: "Platinum I",
    21: "Diamond V",
    22: "Diamond IV",
    23: "Diamond III",
    24: "Diamond II",
    25: "Diamond I",
    26: "Ruby V",
    27: "Ruby IV",
    28: "Ruby III",
    29: "Ruby II",
    30: "Ruby I",
    31: "Master",
}


def make_problem_content(template, problem: dict) -> str:
    return template\
        .replace('<problem_name>', problem['name']) \
        .replace('<problem_id>', str(problem['id'])) \
        .replace('<url>', problem['url']) \
        .replace('<difficulty>', problem['difficulty']) \
        .replace('<tags>', ', '.join(problem['tags'])) \



def write_all_text(path: str, text: str) -> None:
    f = open(path, 'w')
    f.write(text)
    f.close()


def get_problems(problems: list) -> list:
    """문제 정보를 담고 있는 딕셔너리를 반환합니다.
    """
    if len(problems) < 1:
        raise ValueError("Invalid number of problems")

    url = f"https://solved.ac/api/v3/problem/lookup?problemIds={','.join(problems)}"
    response = urllib.request.urlopen(url)
    source = response.read()

    # if response.status_code != 200:
    #     raise Exception("Unexpected response status")

    json_data = json.loads(source)
    problems = []

    for problem in json_data:
        problem_info = defaultdict(str)
        problem_info["id"] = problem["problemId"]
        problem_info["name"] = html.unescape(problem["titleKo"])
        problem_info["level"] = problem["level"]
        problem_info["difficulty"] = __tier_text[problem["level"]]
        problem_info["url"] = f"https://www.acmicpc.net/problem/{problem['problemId']}"
        # language ko만 추출
        if problem["tags"] is not None:
            tags = [x["displayNames"] for x in problem["tags"]]
            problem_info["tags"] = [x["name"]
                                    for tags in tags for x in tags if x["language"] == 'ko']
        problems.append(problem_info)

    return problems

# response = requests.get("https://solved.ac/api/v3/problem/show?problemId=1052")
# json_data = response.json()


class CommandLineParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description="백준 문제 가져오기 사용법")

        parser.add_argument("-p", "--problems", nargs='+',
                            help="사용법 -p 1052 3023", required=True, default="")
        parser.add_argument(
            "-w", "--week", help="사용법: -w (week폴더이름) ex: week1", required=True, default="")
        parser.add_argument(
            "-n", "--name", help="사용법: -n 자신의 이름", required=True, default="")
        try:
            self.__problems = None
            self.__week = None
            self.__name = None
            argument = parser.parse_args()

            if argument.problems:
                try:
                    self.__problems = argument.problems
                except:
                    print("문제번호는 숫자로 기입해주세요.")
            if argument.week:
                self.__week = argument.week
            if argument.name:
                self.__name = argument.name
        except:
            parser.print_help()

    def validation(self):
        return self.__problems is not None and self.__week is not None and self.__name is not None

    def problems(self):
        return self.__problems

    def save_dir(self):
        return self.__name

    def week_dir(self):
        return self.__week


def execute(app: CommandLineParser) -> None:
    if app.validation():
        problems = app.problems()
        # 이름 폴더
        save_dir = app.save_dir()
        # 주 단위 폴더
        week_dir = app.week_dir()

        # 입력받은 이름 폴더 ( abs path )
        target_dir = os.path.join(os.getcwd(), save_dir)
        abs_week_dir = os.path.join(target_dir, week_dir)
        if not os.path.isdir(target_dir):
            print(f"{save_dir} 디렉터리가 존재하지 않습니다.")
            return

        # if os.path.isdir(os.path.join(target_dir, week_dir)):
        #     print(f"입력한 디렉터리 -{week_dir}이 이미 존재합니다.")
        #     return
        if not os.path.isdir(abs_week_dir):
            os.mkdir(abs_week_dir)

        print("문제 정보를 생성합니다.")

        problems_info = get_problems(problems)
        for problem in problems_info:
            content = make_problem_content(__template, problem)
            problem_dir = os.path.join(
                abs_week_dir, f"[{problem['id']}]{problem['name']}")
            if not os.path.isdir(problem_dir):
                os.mkdir(problem_dir)

            write_all_text(os.path.join(
                problem_dir, f"{problem['id']}.py"), content)

        print(problems_info)


if __name__ == '__main__':
    app = CommandLineParser()

    execute(app)
