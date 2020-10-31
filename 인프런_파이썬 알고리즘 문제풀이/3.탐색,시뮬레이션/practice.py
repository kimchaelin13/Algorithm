import sys
sys.stdin=open('input.txt','r')


for tc in range(1,11):
    n=int(input())
    board=[list(input()) for _ in range(8)]

    cnt=0
    for i in range(8-n+1):
        for j in range(8):
            tmp=board[j][i:i+n]
            if tmp==tmp[::-1]:
                cnt+=1
        for k in range(n//2):
            if board[i+k][j] != board[i+n-k-1][j]:
                break
        else:
            cnt+=1
    print(cnt)
