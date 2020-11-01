import sys
sys.stdin=open('input.txt','r')

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def make_arr(arr):
    d=0
    r=0
    c=0
    num=1

    while num<=N*N:
        arr[r][c]=num
        num+=1

        nr=r+dx[d]
        nc=c+dy[d]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
            r,c=nr,nc
        else:
            d=(d+1)%4
            r+=dx[d]
            c+=dy[d]
    return arr


for tc in range(1,int(input())+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    #print(arr)
    result=make_arr(arr)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(result[i][j],end=" ")
        print()