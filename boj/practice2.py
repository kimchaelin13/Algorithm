import sys
sys.stdin=open('input.txt','r')

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

#1.날짜를 기록해야함=> 같은 크기의 dist배열 만들어야지
    입력받고, 행렬 리스트 만듦
    
#2.1을 찾으면, Q에 넣고, 그 상태로 돌려야 함.

    
    사방탐색 => 만약에 arr[ni][nj]==0, 범위 안에 있으면 => dist[ni][nj]=dist[pi][pj]+1
    그리고 방문표시(토마토 익었으면)=>익었다고 표시
#3. 출력은 최대 dist value에서 -1
'''

from collections import deque

di=[-1,1,0,0]
dj=[0,0,-1,1]

M,N=map(int,input().split())
farm=[list(map(int,input().split())) for _ in range(N)]
dist=[[0]*M for _ in range(N)]
Q=deque()

for i in range(N):
    for j in range(M):
        if farm[i][j]==1:
            Q.append((i,j))

while Q:
    pi,pj=Q.popleft()
    for d in range(4):
        ni=pi+di[d]
        nj=pj+dj[d]
        if 0<=ni<N and 0<=nj<M and farm[ni][nj]==0:
            farm[ni][nj]=1
            dist[ni][nj]=dist[pi][pj]+1
            Q.append((ni,nj))

flag=1
for i in range(N):
    for j in range(M):
        if farm[i][j]==0:
            flag=0
result=0
#flag=1이라는 뜻은 안익은 토마토가 없다는뜻
if flag==1:
    for i in range(N):
        for j in range(M):
            if dist[i][j]>result:
                result=dist[i][j]
    print(result)
else:
    print(-1)