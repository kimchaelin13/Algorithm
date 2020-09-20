import sys
sys.stdin = open("input.txt", "r")

'''

'''

# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
#
# def DFS(x,y):
#     global cnt
#     if x==4 and y==4:
#         cnt+=1
#
#     else:
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<=4 and 0<=ny<=4 and check[nx][ny]==0 and board[x][y] < board[nx][ny]:
#                 check[nx][ny]=1
#                 DFS(nx,ny)
#                 check[nx][ny]=0
#
# if __name__=='__main__':
#     N=int(input())
#     check=[[0]*N for _ in range(N)]
#     board=[list(map(int,input().split())) for _ in range(N)]
#     #최소좌표가 어딨는지 찾아야되는데 일단 복잡할것같아서 0,0으로 하고 넘어가야지
#     check[0][0]=1
#     cnt=0
#     DFS(0,0)
#     print(cnt)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1

    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny]==0:
                if board[x][y] < board[nx][ny]:
                    check[nx][ny]=1
                    DFS(nx,ny)
                    check[nx][ny]=0

if __name__ == '__main__':
    n=int(input())
    board=[list(map(int,input().split())) for _ in range(n)]
    check=[[0]*n for _ in range(n)]
    max=-98765
    min=98765
    sx=0
    sy=0
    for i in range(n):
        for j in range(n):
            if board[i][j] < min:
                min=board[i][j]
                sx=i
                sy=j
    ex=0
    ey=0
    for i in range(n):
        for j in range(n):
            if board[i][j] > max:
                max=board[i][j]
                ex=i
                ey=j
    check[sx][sy]=1
    cnt = 0
    DFS(sx,sy)
    print(cnt)