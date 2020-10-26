import sys
sys.stdin = open("input.txt", "r")
dr=[-1,1,0,0]
dc=[0,0,-1,1]

def BFS(i,j):
    global ans

    queue=[(r,c)]
    visited[r][c]=1

    while len(queue)>0:
        curr_r,curr_c=queue.pop(0)

        for i in range(4):
            nr=curr_r+dr[i]
            nc=curr+c+dc[i]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] or maze[nr][nc]=='1':
                continue

            if maze[nr][nc] =='3':
                ans=1
                return

            queue.append((nr, nc))
            visited[nr][nc] = 1


for tc in range(1,11):
    input()
    N=100
    maze=[list(input()) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    ans=0

    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                BFS(i,j)

    print("#{} {}".format(tc,ans))