import sys
sys.stdin = open("input.txt", "r")

dx=[-1,]
def dfs(x,y):


for tc in range(1,int(input())+1):
    n=int(input())
    board=[list(map(int,input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                dfs(i,j)

