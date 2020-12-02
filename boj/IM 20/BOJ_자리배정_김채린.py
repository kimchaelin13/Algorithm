import sys
sys.stdin=open('input.txt','r')

'''
7 6
. 만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력해야 한다. 
'''
di=[0,1,0,-1]
dj=[1,0,-1,0]

N,M=map(int,input().split())
arr=[[0]*M for _ in range(N)]
find=int(input())

if find>N*M:
    print(0)

num=1
d=0
i,j=0,0

while num<=N*M:
    arr[i][j]=num

    num+=1

    ni,nj=i+di[d], j+dj[d]

    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
        i=ni
        j=nj
    else:
        d=(d+1)%4
        i+=di[d]
        j+=dj[d]
flag=0
for r in range(N):
    for c in range(M):
        if find==arr[r][c]:
            print(r+1,c+1)
            flag=1
            break
    if flag:
        break
