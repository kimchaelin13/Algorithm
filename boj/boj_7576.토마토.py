
'''
#1.입력받고 (배열받고)
#2.dist배열 0으로 초기화한 것 만듦. 여기에 일수를 체크할것
#3.배열 돌면서 1인곳이 있으면 bfs(i,j), 그리고 여기는 dist[i][j]=1
#4.내가 만들 프로그램은 dist를 모두 완성시키는 프로그램

'''
import sys
from collections import deque
sys.stdin=open('input.txt','r')

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j):
    dist[i][j]=1

    while Q:
        px,py=Q.popleft()
        for d in range(4):
            nx=px+dx[d]
            ny=py+dy[d]
            if 0<=nx<N and 0<=ny<M and farm[nx][ny]==0:
                farm[nx][ny]=1
                Q.append((nx,ny))
                dist[nx][ny]=dist[px][py]+1

M,N=map(int,input().split())
farm=[list(map(int,input().split())) for _ in range(N)]
dist=[[0]*M for _ in range(N)]
Q=deque()
for i in range(N):
    for j in range(M):
        if farm[i][j]==1:
            Q.append((i,j))
            bfs(i,j)

print(dist)
flag=1
for i in range(N):
    for j in range(M):
        if dist[i][j]==0 and farm[i][j]==0:
            flag=0

result=0
if flag==1:
    for i in range(N):
        for j in range(M):
            if dist[i][j]>result:
                result=dist[i][j]
    print(result-1)
else:
    print(-1)