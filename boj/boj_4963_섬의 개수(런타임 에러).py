import sys
sys.stdin=open('input.txt','r')
from collections import deque

'''
#bfs로 풀어야지 ㅁㅊ 이것도 틀림 도랏나,,,(유기농 배추랑 같이 몰랑

#1.입력 똑같이 받고, dist배열 준비함
#2.for문 조회하다가 땅이 있고,dist가 0이면, 출발
#3.
'''
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def bfs(x,y):
    arr[x][y]=0
    Q=deque()
    Q.append((x,y))

    while Q:
        x,y=Q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1 and dist[nx][ny]==0:
                dist[nx][ny]=dist[x][y]+1
                Q.append((nx,ny))


while True: #충격적..
    M,N=map(int,sys.stdin.readline().split())
    if M==0 and N==0:
        break #언제 테케가 끝날지 몰라서 break로 해야함
    arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    dist=[[0]*M for _ in range(N)]
    #print(arr)
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1 and dist[i][j]==0:
                bfs(i,j)
                cnt+=1
    print(cnt)



'''
아이스크림찾기였나? 그거랑 매 우 유 사 하다
뭉탱이를 찾는거임 근데 ! 대각선까지 추가

#1. 배열 받고, 행렬 입력받음(1은 땅, 0은 바다)
#2. 그 배열을 순회하면서 1을 찾으면 그때 섬 한개를 찾아주는 함수를 실행시킨다.
#2-1. 체크배열 안만드는 대신 방문한 배열은 2로 만들어버림

#3. 다 찾으면 다시 아래로 내려옴. 그러면 그때 cnt를 +1

#? 여기는 0,0이 있는데 이걸 어떻게 처리해야하는거지?? -> while문으로 ,,

#근데 런타임에러났다..how to handle....................


dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def check(x,y):
    arr[x][y]=2

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1:
            #방문했다
            arr[nx][ny]=2
            check(nx,ny)

while True: #충격적..
    M,N=map(int,sys.stdin.readline().split())
    if M==0 and N==0:
        break #언제 테케가 끝날지 몰라서 break로 해야함
    arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    #print(arr)
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                check(i,j)
                cnt+=1
    print(cnt)
'''