import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
#1. 배열을 받는다
#2. (0,0)부터 출발해서 => (N,M)까지 가는건데, [n][m]을 출력하면 되나??
    (거리를 다 써붙이는건가???) 
    bfs좀 공부하자!!!!!!!!!!!!!!!
'''
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def BFS(x,y):
    Q=deque()
    Q.append((x,y))

    while Q:
        x,y=Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                Q.append((nx,ny))

if __name__=='__main__':
    N,M=map(int,input().split())
    arr=[list(map(int,input())) for _ in range(N)]
    BFS(0,0)
    print(arr[N-1][M-1])

