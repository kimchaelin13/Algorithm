import sys
sys.stdin = open("input.txt", "r")

# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# def dfs(x,y):
#     ch[x][y]=1
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<M and 0<=ny<N and ch[nx][ny]==0 and board[nx][ny]==1:
#             ch[nx][ny] = 1
#             dfs(nx,ny)
#
# for tc in range(int(input())):
#     M,N,K=map(int,input().split())
#     board=[[0]*N for _ in range(M)]
#     ch=[[0]*N for _ in range(M)]
#     cnt=0
#     for _ in range(K):
#         x,y=map(int,input().split())
#         board[x][y]=1
#     for i in range(M):
#         for j in range(N):
#             if board[i][j]==1:
#                 dfs(i,j)
#                 cnt+=1
#     print(cnt)


T=int(input())
for tc in range(T):
    cnt=0
    M,N,K=map(int,input().split())
    land=[[0]*(M+2) for _ in range(N+2)]

    for k in range(K):
        a,b=map(int,input().split())
        land[j+1][i+1]=1
    for j in range()