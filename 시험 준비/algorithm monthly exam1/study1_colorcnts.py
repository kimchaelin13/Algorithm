import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    board=[[0]*N for _ in range(N)]

    for _ in range(M):
        cnt=0
        x1,y1,x2,y2=map(int,input().split())

        for r in range(x1,x2+1):
            for c in range(y1,y2+1):
                if board[r][c] == 0:
                    board[r][c] +=1

    for r in range(N):
        for c in range(N):
            if board[r][c]==1:
                cnt+=1
    print('#{} {}'.format(tc,cnt))