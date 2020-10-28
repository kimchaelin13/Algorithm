import sys
sys.stdin=open('input.txt','r')
'''
#1.N이 5고, M이 3이면, 5-3=2 인덱스까지만 돌면서 더해줘야함.
#2.tmp만들고, res만들어서 기존의 res보다 tmp가 더 크다면/ res=tmp 로 갱신 
'''
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]

    res=0
    for r in range(0,N-M+1):
        for c in range(0,N-M+1):
            total=0
            for m in range(M):
                total+=sum(arr[r+m][c:c+M])
            if total>res:
                res=total
    print('#{} {}'.format(tc,res))

