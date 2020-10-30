import sys
sys.stdin=open('input.txt','r')
'''
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

#1.5*5 배열 받고
#2.3*3에 해당하는 네모만 돌면서 합을 구하고
    그 합보다 커서 갱신되는 최종 res를 구한다 
'''


for tc in range(1,int(input())+1):
    N,K=map(int,input().split())
    flies=[list(map(int,input().split())) for _ in range(N)]
    res=0
    for r in range(0,N-K+1):
        for c in range(0,N-K+1):
            tmp=0
            for k in range(K):
                tmp+= sum(flies[r+k][c:c+K])

            if tmp>res:
                res=tmp

    print('#{} {}'.format(tc,res))

