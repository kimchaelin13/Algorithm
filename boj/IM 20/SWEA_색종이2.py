import sys
sys.stdin=open('input.txt','r')

'''
1을 발견하면 -> 함수를 돌리는데
이함수는 주변에 0이 있는지 확인하고, 0이 있으면 ans에 더해주고, 끝
'''
dr=[-1,1,0,0]
dc=[0,0,-1,1]
def check(r,c):
    global ans
    for d in range(8):
        nr=r+dr[d]
        nc=c+dc[d]
        if 0<=nr<N and 0<=nc<N and board[nr][nc]==0:
            ans+=1
        elif 0>nr or nr==N or 0>nc or nc==N:
            ans +=1

N=100
board=[[0]*N for _ in range(N)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    xx,yy=x+10,y+10
    #보드 입력을 받고, 보드에 색종이가 있는 부분을 1로 만든다
    for r in range(x,xx):
        for c in range(y,yy):
            board[r][c]=1
ans=0
for r in range(N):
    for c in range(N):
        #1을 찾으면 그게 0이나 99인덱스에 있는지 확인한다-> 있으면 +1
        if board[r][c]==1:
            check(r,c)
print(ans)



'''

di=[-1,1,0,0]
dj=[0,0,-1,1]
def check(i,j):
    global ans
    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]
        if 0<=ni<N and 0<=nj<N and board[ni][nj]==0:
            ans+=1
        elif ni<0 or ni==N or nj<0 or nj==N:
            ans+=1

N=100
board=[[0]*N for _ in range(N)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
                board[i][j]=1

ans=0
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            check(i,j)
print(ans)
'''