import sys
sys.stdin=open('input.txt','r')

'''
#1.입력울 받음
#2.이미 폭탄이 어디 좌표에서 터질지 초기폭탄좌표가 주어졌기 때문에 바로 cnt_bomb(i,j)를 실행시킴
#3.그 프로그램은 지도에서 폭탄이 몇개 터졌는지 세어줄 역할을 할거고, 그 개수를 return 할 것이다
    bombMap[i][j]에 있는 value값만큼 돌게 해야한다(while)
    nx,ny를 할때 while value<=bombmap[i][j]만큼/value=1에서 시작해서 한번하면 value+=1
    
    한번 방문(폭발)한곳은 다시 또 세면 안되니까 0으로 바꿔버리기
    
'''
dx = [0,0,1,-1] #우좌하상
dy = [1,-1,0,0]
def cnt_bomb(x,y):
    global cnt
    visited[x][y]=True

    for k in range(4):
        for c in range(1,arr[x][y]+1):
            nx=x+dx[k]*c
            ny=y+dy[k]*c
            # if 0<=nx<N and 0<=ny<N and arr[nx][ny]!=0 and visited[nx][ny]==False:
            #     cnt+=1
            #     cnt_bomb(nx,ny)
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if visited[nx][ny]==True:
                continue
            if arr[nx][ny] == 0:
                continue
            cnt+=1
            cnt_bomb(nx,ny)


for tc in range(1,int(input())+1):
    N=int(input())
    i,j=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[False]*N for _ in range(N)]
    cnt=1
    cnt_bomb(i,j)
    print(cnt)

