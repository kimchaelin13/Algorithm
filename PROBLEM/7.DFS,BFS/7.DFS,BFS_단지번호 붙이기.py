import sys

sys.stdin = open("input.txt", "r")


# <dfs>
# 단지뭉텅이의 수를 세야함 그리고 단지뭉텅이안에있는 개수를 세야한다.


dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
    cnt+=1
    board[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny]==1:
            DFS(nx,ny)

if __name__ == '__main__':
    n=int(input())
    board=[list(map(int,input())) for _ in range(n)]
    res=[]

    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0 #단지발견하면 그안에 세줄것
                DFS(i,j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)

