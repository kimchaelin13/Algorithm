import sys
sys.stdin=open('input.txt','r')

from collections import deque
import copy
di=[-1,1,0,0]
dj=[0,0,1,-1]
def cnt(i,j):
    cnt=0
    checked = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] !=0 and checked[i][j]==False:
                cnt+=1
                Q=deque()
                Q.append((i,j))

                while Q:
                    x,y=Q.popleft()
                    checked[x][y]=True
                    for d in range(4):
                        ni = x+di[d]
                        nj = y+dj[d]
                        if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=0 and checked[ni][nj]==False:
                            checked[ni][nj]=True
                            Q.append((ni,nj))
    return cnt

def minus(check_sea):
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                sea = 0

                for d in range(4):
                    ni=i+di[d]
                    nj=j+dj[d]
                    if 0<=ni<N and 0<=nj<M and check_sea[ni][nj]==0:
                        arr[i][j]-=1
                        if 0>arr[i][j]:
                            arr[i][j]=0
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
year=0
while True:
    if cnt(0,0)>=2:
        break
    else:
        year+=1
        check_sea = copy.deepcopy(arr)
        minus(check_sea)
print(year)