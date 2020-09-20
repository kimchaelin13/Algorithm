import sys
from collections import deque
sys.stdin = open("input.txt", "r")
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#m이 행번호고, n이 열번호다
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(m)]
dis=[[0]*n for _ in range(m)]
Q=deque()

for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            Q.append((i,j))

while Q:
    tmp=Q.popleft()
    for k in range(4):
        ni=tmp[0]+dx[k]
        nj=tmp[1]+dy[k]
        if 0<=ni<m and 0<=nj<n and board[ni][nj]==0:
            board[ni][nj]=1
            dis[ni][nj]=dis[tmp[0]][tmp[1]]+1
            Q.append((ni,nj))

flag=1
res=0
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            flag=0
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>res:
                res=dis[i][j]
    print(res)
else:
    print(-1)

