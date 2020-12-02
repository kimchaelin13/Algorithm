import sys
sys.stdin=open('input.txt','r')

dr=[0,1,0,-1]
dc=[1,0,-1,0]
for tc in range(1,int(input())+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    num=1
    r,c=0,0
    d = 0
    while N*N>=num:
        arr[r][c] = num
        #다음숫자
        num+=1
        #다음좌표
        nr = r+dr[d]
        nc = c+dc[d]

        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
            r,c = nr,nc
        else:
            d=(d+1)%4
            r=r+dr[d]
            c=c+dc[d]

    print('#{}'.format(tc))
    for x in arr:
        print(*x)


