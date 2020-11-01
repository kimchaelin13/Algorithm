import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N=int(input())
    board=[[0]*10 for _ in range(10)]
    sum=0
    for i in range(N):
        x1,y1,x2,y2,color = map(int,input().split())

        for r in range(x1,x2+1):
            for c in range(y1,y2+1):
                board[r][c]+=color

    # for r in range(10):
    #     for c in range(10):
    #         if board[r][c]==3:
    #             sum += 1
    for i in board:
        sum+=i.count(3)

    print('#{} {}'.format(tc,sum))
