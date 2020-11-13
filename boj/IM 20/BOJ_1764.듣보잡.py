#res가 2면 걔 출력
import sys
sys.stdin=open('input.txt','r')


N,M=map(int,input().split())
name=[]
for _ in range(N+M):
    name.append(input())
cnt=1
res=[]
for i in range(N+M-1):
    for j in range(i+1,N+M):
        if name[i]==name[j]:
            cnt+=1
            res.append(name[i])
print(cnt)
for i in sorted(res):
    print(i)

