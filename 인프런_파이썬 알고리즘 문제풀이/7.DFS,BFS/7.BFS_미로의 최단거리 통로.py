import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[list(map(int,input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)] #(7,7)
Q=deque()
Q.append((0,0)) #시작점
#한번 방문한 곳은 다시 방문못하게 벽이되도록!
# 1으로 만들어버리면 벽이되는 효과, 체크배열대신 이렇게 쓰자
board[0][0] = 1

while Q: #Q가 비면 거짓이 되서 멈춘다
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))

#벽으로 가로막혀서 못왔다는거임 그러면 -1을 출력하세요라고 문제
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

