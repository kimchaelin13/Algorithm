import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(m)]
Q=deque()
dis=[[0]*n for _ in range(m)] #거리, 날짜를 여기 저장할거임

for i in range(m): #행번호니까 m
    for j in range(n):
        if board[i][j]==1:
            Q.append((i,j))

while Q:
    tmp=Q.popleft()
    for k in range(4):
        ni=tmp[0]+dx[k]
        nj=tmp[1]+dy[k]
        #행번호가 m이고 열번호가 n!!
        if 0<=ni<m and 0<=nj<n and board[ni][nj]==0:
            board[ni][nj]=1
            dis[ni][nj]=dis[tmp[0]][tmp[1]]+1
            Q.append((ni,nj))

flag=1
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            flag=0
result=0
#flag=1이라는 뜻은 안익은 토마토가 없다는뜻
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1)





