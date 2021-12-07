N, K = map(int, input().split())

jose=[i for i in range(1, N+1)]
#N크기의 리스트 생성

result=[]

seqNo = K-1
while len(jose):
    if seqNo>=len(jose):
        seqNo=seqNo%len(jose)
    else:
        result.append(str(jose.pop(seqNo)))
        seqNo+=(K-1)

print("<", ", ".join(result), ">", sep='')