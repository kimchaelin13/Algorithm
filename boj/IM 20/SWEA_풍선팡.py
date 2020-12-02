import sys
sys.stdin=open('input.txt','r')

'''
3
3 5
2 1 1 2 2 
2 2 1 2 2 
2 2 1 1 2 
'''
dr=[-1,1,0,0]
dc=[0,0,-1,1]
def calc(i,j):
    global MAX
    temp_sum=arr[i][j]

    for k in range(1,arr[i][j]+1):
        for d in range(4):
            ni = i + dr[d]*k
            nj = j + dc[d]*k
            if 0<=ni<N and 0<=nj<M:
                temp_sum += arr[ni][nj]
    if temp_sum>MAX:
        MAX=temp_sum


for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    MAX=0
    for i in range(N):
        for j in range(M):
            calc(i,j)
    print('#{} {}'.format(tc,MAX))