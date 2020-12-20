import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
cnt=0 #섬의 개수
# res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0 #다시 안올거니까 체크
            Q.append((i,j))
            # cnt=1
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    ni=tmp[0]+dx[k]
                    nj=tmp[1]+dy[k]
                    if 0<=ni<n and 0<=nj<n and board[ni][nj]==1:
                        board[ni][nj]=0
                        Q.append((ni,nj))
            # while문 하나를 돌고나면 bfs가 끝나는거임!
            # 섬하나를 찾은거임
            cnt+=1
print(cnt)