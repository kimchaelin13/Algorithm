import sys
sys.stdin=open('input.txt','r')

N=int(input())
arr=[[0]*N for _ in range(N)]

n=1
for j in range(N):
    for i in range(N):
        arr[i][j]=n
        n+=1
for x in arr:
    print(*x)