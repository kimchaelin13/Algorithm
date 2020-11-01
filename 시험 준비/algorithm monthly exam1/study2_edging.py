import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    result=[]
    for r in range(N-K+1):
        for c in range(M-K+1):
            total_s=0
            minus_s=0
            for k in range(K):
                total_s += sum(board[r + k][c:c + K])

                if k != 0  and k != K-1:
                    minus_s += sum(board[r + k][c+1:c+K-1])

            result.append(total_s-minus_s)
    print('#{} {}'.format(tc,max(result)))




