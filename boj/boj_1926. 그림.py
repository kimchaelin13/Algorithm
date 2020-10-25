import sys
sys.stdin=open('input.txt','r')
from collections import deque
'''
단지번호랑 똑같다.

1.입력받고,리스트 만들고 시작
2.2차원 배열 순회하면서 1을 찾으면 거기서 시작
3.res=[]만들어놓고,
4.내가 만들 프로그램은 그림안에 있는 넓이를 구해주는 함수다
    그리고 그 넓이를 리턴함
5. 돌아와서는 res.append(return) 

'''
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def get_largest(x,y):
    cnt=1
    board[x][y]=0
    Q=deque()
    Q.append((x,y))

    while Q:
        px,py=Q.popleft()
        for d in range(4):
            nx=px+dx[d]
            ny=py+dy[d]
            if 0<=nx<N and 0<=ny<M and board[nx][ny]==1:
                board[nx][ny]=0
                cnt+=1
                Q.append((nx,ny))
    return cnt

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(M+1)]
result=[]
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            result.append(get_largest(i,j))

a,b=len(result), max(result)
if a==0:
    b=0
    print(a)
    print(b)
else:
    print(a)
    print(b)