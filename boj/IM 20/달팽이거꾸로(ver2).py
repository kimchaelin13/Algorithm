import sys
sys.stdin=open('input.txt','r')
'''
N=7일때 d는 8번 바뀐다

d=0 1칸
d=1 1칸
d=2 2칸
d=3 2칸
d=0 3칸
d=1 3칸
d=2 4칸
d=3 4칸
d=0 4칸
'''
di=[0,-1,0,1]
dj=[-1,0,1,0]

N=5
arr=[[0]*N for _ in range(N)]

i=N//2
j=N//2

num=1
size=N+1 #

d = 0
s = 1
t = 1
while num<=N*N:
    arr[i][j]=num

    #next num
    t=1
    while t<=s:
        if num > N*N:
            break
        num += 1
        # pos next num
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            arr[ni][nj]=num
            i=ni
            j=nj
            t+=1

    #처음에 가야하는 스텝이 s다
    #그리고 d==0, d==3일때마다 s+1를 한다
    #그리고 조건에 t가 s와 같아질때까지, 가게함
    #t는 1부터 시작해서 ~ 움직일때마다 +1을 해줄것
    if d==1 or d==3:
        s+=1
    d=(d+1)%4


for x in arr:
    print(x)

