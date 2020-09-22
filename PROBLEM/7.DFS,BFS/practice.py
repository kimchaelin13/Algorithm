import sys
from collections import deque
sys.stdin = open("input.txt", "r")

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y,h):

    ch[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and board[nx][ny]>h:
            DFS(nx,ny,h)

if __name__=='__main__':
    n=int(input())
    cnt=0
    res=0
    board=[list(map(int,input().split())) for _ in range(n)]
    #단지번호,섬나라를 100번한다고보면됨
    #보드를 건들면 안됩니다
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0
        #h안에서 이중for문 도는거다
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    #h보다 클때만 뻗어나가는거니까 같이 넘겨줌
                    DFS(i,j,h)
        res=max(res,cnt)
        if cnt==0:
            break
    print(res)

