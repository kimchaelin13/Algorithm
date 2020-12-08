import sys
sys.stdin=open('input.txt','r')

N,M=map(int,input().split())
arr=[[0]*M for _ in range(N)]

num=1
for i in range(N):
    for j in range(M):
        if i%2==0:
            arr[i][j]=num
        else:
            j=M-1-j
            arr[i][j]=num
        num+=1

for x in arr:
    print(*x)