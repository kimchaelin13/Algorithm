import sys
sys.stdin=open('input.txt','r')
from pprint import pprint


dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
    cnt+=1
    arr[x][y]=2

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<len(arr[0]) and 0<=ny<len(arr) and arr[nx][ny]==1:
            DFS(nx,ny)


if __name__=='__main__':
    C,R=map(int,input().split())
    N=int(input())
    arr=[[1]*C for _ in range(R)]
    arr.insert(0,[0]*C)
    arr.append([0]*C)

    for x in arr:
        x.insert(0,0)
        x.append(0)

    for _ in range(N):
        dir, idx = map(int,input().split())

        if dir==0:
            arr.insert(idx+1,[0]*(len(arr[0])))
        else:
            for x in arr:
                x.insert(idx+1,0)

    res=[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==1:
                cnt=0
                DFS(i,j)
                res.append(cnt)
    print(max(res))





