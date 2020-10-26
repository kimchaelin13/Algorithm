import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]
N,M=map(int,input().split())
board=[list(map(int,input())) for _ in range(N)]
dist=[[0]*M for _ in range(N)]
dist[0][0]=1
Q=deque()
Q.append((0,0))
board[0][0]=0 #방문했으니까 0으로 만들거임

while Q:
    tmp=Q.popleft()
    for i in range(4):
        nx=tmp[0]+dx[i]
        ny=tmp[1]+dy[i]
        if 0<=nx<N and 0<=ny<M and board[nx][ny]==1:
            board[nx][ny]=0
            dist[nx][ny]=dist[tmp[0]][tmp[1]]+1
            Q.append((nx,ny))

print(dist[N-1][M-1])

