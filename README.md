# 엘코테

## 👨‍👧 Contributors

| A반                                           | B반                                                 |
| --------------------------------------------- | --------------------------------------------------- |
| [alexYooDev](https://github.com/alexYooDev)   | [sy109](https://github.com/sy109)                   |
| [castela0119](https://github.com/castela0119) | [serajang99](https://github.com/serajang99)         |
| [seonkyena](https://github.com/seonkyena)     | [julia98percent](https://github.com/julia98percent) |
| [Toni-NKim](https://github.com/Toni-NKim)     | [HyeongSeoku](https://github.com/HyeongSeoku)       |
| [wkdal904](https://github.com/wkdal904)       | [rmsqor103](https://github.com/rmsqor103)           |
| [2ykwang](https://github.com/2ykwang)         |                                                     |

## 📁 파일 및 폴더 구조

규칙: `(이름)/(해당주차)/[(문제번호)](문제이름)/파일`

*예시:*

- `이름/week1/[1874]스택수열/solve.py`
- `이름/week2/[1874]스택수열/README.md`

단순한 예시이며 파일이름은 자유형식 입니다.

폴더와 파일을 생성하시는게 번거로우시다면 아래 스크립트를 사용하시면 됩니다.

*사용법*
```shell
$ python fetch_problem.py -p 문제번호1 문제번호2 ... -n 자신의이름 -w (해당주차)

   # ex:)

$ python fetch_problem.py -p 1068 1747 2960 -n "이름" -w "week3"
```

명령어를 실행하시면 자신의 디렉터리에 입력으로 받은 문제 폴더가 생성됩니다.

<br>

## 📑 커밋 규칙

아래 가이드를 참고해주세요.

<details markdown="1">
   <summary>
      <samp>Commit Guide</samp>
   </summary>
   <h3 id="1-clone-">1. 원격 저장소 Clone 하기</h3>
   <p><code>git clone https://github.com/elcote/elice-coding-test.git</code></p>
   <h3 id="2-">2. 로컬 저장소에 자신의 브랜치 생성하기</h3>
   <ul>
      <li><code>git branch (자신의영문이름)</code></li>
      <li><code>git checkout (자신의영문이름)</code></li>
   </ul>
   <p>브랜치를 생성한 뒤 생성한 브랜치를 checkout 합니다.</p>
   <h3 id="3-">3. 로컬에 생성한 브랜치를 원격 저장소에 반영하기</h3>
   <p>본인의 이름으로 생성한 브랜치를 체크아웃 한 상태에서 <code>git add</code>, <code>git commit</code> 까지 완료된 상태라면 아래에 명령어로 원격저장소에 브랜치를 추가할 수 있습니다.</p>
   <ul>
      <li><code>git push origin (자신의영문이름)</code> 생성한 브랜치를 원격 저장소에 푸시 합니다.</li>
   </ul>
   <h3 id="4-master-">4. 자신의 브랜치를 master 브랜치와 병합하기</h3>
   <ul>
      <li><code>git checkout master</code></li>
      <li><code>git pull</code> master 브랜치의 가장 최근 데이터를 가져옵니다. (충돌을 막기 위함)</li>
      <li><code>git merge (자신의영문이름)</code> master 브랜치와 자신의 브랜치를 병합 합니다.</li>
      <li><code>git push origin master</code> 병합된 master 브랜치를 원격 저장소에 push 합니다.</li>
   </ul>
</details>
<br>

...

## 📚 스터디 규칙

...
