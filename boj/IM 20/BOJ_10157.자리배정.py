import sys
sys.stdin=open('input.txt','r')

'''
7 6
11

'''
di=[0,1,0,-1]
dj=[1,0,-1,0]

R,C=map(int,input().split())
N=int(input())
arr = [[0]*C for _ in range(R)]

i=0
j=0
d=0

num=1
'''
만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력해야 한다. 
'''
if N > R*C:
    print(0)
while num <=R*C:

    arr[i][j]=num

    num+=1

    ni = i+di[d]
    nj = j+dj[d]

    if 0<=ni<R and 0<=nj<C and arr[ni][nj]==0:
        i,j = ni,nj
    else:
        d = (d+1)%4
        i += di[d]
        j += dj[d]

flag=0
# #2.답 출력
for i in range(R):
    for j in range(C):
        if arr[i][j] == N:
            print(i+1,j+1)
            flag=1
            break
    if flag:
        break



