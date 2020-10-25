import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
BFS로 풀기...


#1. 1찾으면 BFS로 올리기
#2. 다시 안가야하니까 숫자 0으로 바꿔버리고
#3. dist배열 만들고
#4. arr[][]에 있는 것 +1 해줌

'''
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    arr[x][y]=0
    Q=deque()
    Q.append((x,y))

    while Q:
        x,y=Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #dist조건이 왜있지
            if 0<=nx<M and 0<=ny<N and arr[nx][ny]==1 and dist[nx][ny]==0:
                dist[nx][ny]=dist[x][y]+1
                Q.append((nx,ny))

for tc in range(int(input())):
    M,N,K=map(int,input().split()) # M 가로 N 세로
    arr=[[0]*(N) for _ in range(M)]
    dist = [[0] * (N) for _ in range(M)]
    for _ in range(K):
        a,b=map(int,input().split())
        arr[a][b]=1
    for x in arr:
        print(x)
    print('_______')
    cnt=0
    for i in range(M):
        for j in range(N):
            #dist 조건이 왜있지?
            if arr[i][j]==1 and dist[i][j]==0:
                cnt += 1
                bfs(i,j)
    for x in dist:
        print(x)
    print(cnt)





'''
#1. tc 입력받고/가로, 세로 입력/ 배추심은 곳 입력받고
#2. 배열크기만큼, 리스트 초기화하고=> for문 돌리면서 1로 표시한다
#3. for문을 돌면서 배열이 1인 곳을 찾으면 dfs(i,j)
#4. 함수로 올라가서는 방문한곳은 2로 만들어버림
#5. 조건에 맞으면, 방문 표시학 dfs(nx,ny)
#6. 함수 밑에는 내려와서 cnt+=1
'''
'''
런타임에러떴다 bfs로 풀어야한다고 하는데

기준이뭐지? 이거 단지번호찾기랑 완전 똑같은데
왜지????

'''
'''
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def DFS(x,y):
    arr[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N and arr[nx][ny]==0:
            arr[nx][ny]=2
            DFS(nx,ny)

for tc in range(int(input())):
    M,N,K=map(int,input().split()) # M 가로 N 세로
    arr=[[0]*(N) for _ in range(M)]

    for _ in range(K):
        a,b=map(int,input().split())
        arr[a][b]=1

    cnt=0
    for i in range(M):
        for j in range(N):
            if arr[i][j]==1:
                DFS(i,j)
                cnt+=1
    print(cnt)
'''


