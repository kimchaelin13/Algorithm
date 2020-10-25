import sys
from collections import deque
sys.stdin=open('input.txt','r')
#이 프로그램은 상하좌우 탐색하면서 갈수있으면 모두 +1를 해서, 그 개수를 return 하는 프로그램
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    cnt=1
    arr[x][y]=0
    Q=deque()
    Q.append((x,y))

    while Q:
        px,py=Q.popleft()
        for k in range(4):
            nx=px+dx[k]
            ny=py+dy[k]
            if 0<=nx<N+1 and 0<=ny<M+1 and arr[nx][ny]==1:
                arr[nx][ny]=0
                cnt+=1
                Q.append((nx,ny))
    return cnt

N,M,K=map(int,input().split())
arr=[[0]*((M+1)) for _ in range(N+1)]
for _ in range(K):
    a,b=map(int,input().split())
    arr[a][b]=1
res=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        #음쓰 하나 찾았으면
        if arr[i][j]==1:
            res.append(bfs(i,j))
print(max(res))