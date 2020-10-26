
import sys
sys.stdin = open("input.txt", "r")

#현우오빠 코드 참고!!! 다시 이해하기!

di=[0,0,1,-1]
dj=[1,-1,0,0]

def BFS(i,j):
    q=[]
    q.append([i,j])
    visited[i][j]=-1 #이게 무슨말일까??

    while q:
        temp=q.pop(0)
        pi,pj=temp[0],temp[1]

        if maze[pi][pj]==3:
            return visited[pi][pj]

        for d in range(4):
            ni=pi+di[d]
            nj=pj+dj[d]

            if ni<0 or ni>=N or nj<0 or nj>=N:
                continue

            if maze[ni][nj]==1:
                continue
            if visited[ni][nj] != 0:
                continue

            q.append([ni,nj])
            visited[ni][nj]=visited[pi][pj]+1
    return 0 ##retur이 여기위치에 있는 이유



for tc in range(1,int(input())+1):
    N=int(input())
    maze=[list(map(int,input())) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    distance=0
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                result=BFS(i,j) #이거 왜 bfs(i,j)가 result가 되는거지???
    print('#{} {}'.format(tc,result))


