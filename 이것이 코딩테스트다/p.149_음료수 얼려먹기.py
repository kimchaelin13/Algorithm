import sys
sys.stdin=open('input.txt','r')

'''
#1. 배열 받기
#2. 0을 먼저 찾아야 함, 0이면 DFS(i,j)출발 
#3. cnt=0으로 초기값 주고, cnt+=1 근데 이걸 어디서 + 해줘야하는건지 헷갈린다.

'''

dr=[-1,1,0,0]
dc=[0,0,-1,1]
def DFS(i,j):
    arr[i][j]=2 #방문처리를 함

    for k in range(4):
        ni=i+dr[k]
        nj=j+dc[k]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            DFS(ni,nj)


if __name__=='__main__':
    N,M=map(int,input().split())
    arr=[list(map(int,input())) for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                DFS(i,j)
                cnt+=1
    print(cnt)

