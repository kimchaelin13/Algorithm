import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
dfs로 하니까 런타임 에러가 났다

bfs로풀어보자
'''
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def cnt_empty(x,y):
    cnt=1
    square[x][y]=1
    Q=deque()
    Q.append((x,y))

    while Q:
        px,py=Q.popleft()
        for k in range(4):
            nx=px+dx[k]
            ny=py+dy[k]
            if 0<=nx<N and 0<=ny<M and square[nx][ny]==0:
                cnt+=1
                square[nx][ny]=1
                Q.append((nx,ny))
    return cnt

if __name__=='__main__':
    M,N,K=map(int,input().split())
    square=[[0]*M for _ in range(N)]
    for _ in range(K):
        x1,y1,x2,y2=map(int,input().split())
        for i in range(x1,x2):
            for j in range(y1,y2):
                square[i][j]=1
    res=[]
    for i in range(N):
        for j in range(M):
            #새로운 뭉탱이를 찾았으면?
            if square[i][j]==0:
                res.append(cnt_empty(i,j))
    print(len(res))
    print(*sorted(res))


'''
#1. 입력받고
#2. M*N 행렬 초기화한다
#3. 직사각형 부분에는 다 1로 바꿔줌

#4. 완성된 행렬 순회하면서 0이면 출발함
#5. cnt_empty(i,j)
#6. 이 함수는 0을 발견하면, 주변에 모두 1로 가로막혀서 갈수없을때까지 다 돌아줄건데, 발견할때마다 cnt+=1 해줘야함
    그리고 한뭉탱이 끝나면 다시 함수종료되고 내려오는데, 그때의 cnt를 어떤 리스트에 담는다
#7. 마지막에 len(res), res.sort()해서 출력함
'''
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# def cnt_empty(x,y):
#     global cnt
#     square[x][y]=1
#     for k in range(4):
#         nx=x+dx[k]
#         ny=y+dy[k]
#         if 0<=nx<N and 0<=ny<M and square[nx][ny]==0:
#             square[nx][ny]=1
#             cnt+=1
#             cnt_empty(nx,ny)
#
# M,N,K=map(int,input().split())
# square=[[0]*M for _ in range(N)]
# for _ in range(K):
#     x1,y1,x2,y2=map(int,input().split())
#     for i in range(x1,x2):
#         for j in range(y1,y2):
#             square[i][j]=1
# res=[]
# for i in range(N):
#     for j in range(M):
#         if square[i][j]==0:
#             cnt=1
#             cnt_empty(i,j)
#             res.append(cnt)
# print(len(res))
# print(*sorted(res))