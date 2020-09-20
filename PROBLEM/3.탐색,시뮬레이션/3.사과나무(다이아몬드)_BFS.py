import sys
from collections import deque
sys.stdin=open('input.txt','r')

di=[-1,0,1,0]
dj=[0,1,0,-1]
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
check=[[0]*n for _ in range(n)]
sum=0

Q=deque()
Q.append((n//2,n//2))
check[n//2][n//2]=1
sum+=board[n//2][n//2]

L=0
while True:
    if L//2:
        break

    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for k in range(4):
            ni=tmp[0]+di[k]
            nj=tmp[1]+dj[k]
            if 0<=ni<n and 0<=nj<n and check[ni][nj]==0:
                check[ni][nj]=1
                sum+=board[ni][nj]
                Q.append((ni,nj))

    L+=1
print(sum)
