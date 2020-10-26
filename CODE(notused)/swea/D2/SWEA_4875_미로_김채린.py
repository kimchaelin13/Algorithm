import sys
sys.stdin = open("input.txt", "r")

di=[0,0,1,-1]
dj=[1,-1,0,0]

def DFS(i,j):
    global result
    visited[i][j]=1

    if maze[i][j]==3:
        result=1
        return
    else:
        for d in range(4):
            ni=i+di[d]
            nj=j+dj[d]

            if ni<0 or ni>=N or nj<0 or nj>=N:
                continue
            if visited[ni][nj]==True:
                continue
            if maze[ni][nj] == 1:
                continue
            DFS(ni,nj)

for tc in range(1,int(input())+1):
    N=int(input())
    maze=[list(map(int,list(input()))) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    result=0

    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                DFS(i,j)
    print('#{} {}'.format(tc,result))