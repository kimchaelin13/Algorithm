import sys
sys.stdin=open('input.txt','r')

'''
6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1
'''
di=[-1,1,0,0]
dj=[0,0,1,-1]
def dfs(i,j,cnt):
    tmp = arr[i][j]
    global MIN, total
    if cnt==3:
        if MIN>total:
            MIN=total

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]
        if 0<=ni<N and 0<=nj<N and checked[ni][nj]==False:
            checked[ni][nj]=True
            tmp += arr[ni][nj]
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
checked = [[False]*N for _ in range(N)]
MIN=987654321
total = 0