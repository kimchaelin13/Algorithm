import sys
sys.stdin = open("input.txt", "r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    global cnt

    #도착지점에 오면 카운팅을 하자
    if x==6 and y==6:
        cnt+=1
    #뻗어나가자
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<=6 and 0<=ny<=6 and board[nx][ny]==0:
                board[nx][ny]=1
                DFS(nx,ny)
                #백하고 뒤돌아왔을때,다시 통로로 바꿔줘야지
                board[nx][ny]=0

if __name__=='__main__':
    board=[list(map(int,input().split())) for _ in range(7)]
    cnt=0
    board[0][0]=1
    DFS(0,0)
    print(cnt)