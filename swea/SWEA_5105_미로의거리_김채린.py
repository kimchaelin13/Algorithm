import sys
sys.stdin = open("input.txt", "r")
di=[0,0,1,-1]
dj=[1,-1,0,0]
def BFS(i,j):
    Q=[]
    Q.append([i,j])
    VISITED[i][j]= -1

    while Q:
        temp=Q.pop(0)
        pi,pj=temp[0],temp[1]

        if MAZE[pi][pj] == 3:
            return VISITED[pi][pj]

        for d in range(4):
            ni=pi+di[d]
            nj=pj+dj[d]

            if ni<0 or ni>=N or nj<0 or nj>=N:
                continue
            if MAZE[ni][nj] == 1:
                continue
            if VISITED[ni][nj] != 0:
                continue
            Q.append([ni,nj])
            VISITED[ni][nj]=VISITED[pi][pj]+1
    return 0


for tc in range(1,int(input())+1):
    N=int(input())
    MAZE=[list(map(int,input())) for _ in range(N)]
    VISITED=[[0]*(N) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if MAZE[i][j] == 2:
                result=BFS(i,j)
    print('#{} {}'.format(tc,result))