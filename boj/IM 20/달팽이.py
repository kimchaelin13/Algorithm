N=5

arr=[[0]*N for _ in range(N)]


di=[0,1,0,-1]
dj=[1,0,-1,0]

num=1

r = 0
c = 0
d = 0
while num<=N*N:
    arr[r][c]=num

    #next num
    num += 1

    #pos next num
    ni=r+di[d]
    nj=c+dj[d]

    if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
        arr[ni][nj]=num
        r=ni
        c=nj
    else:
        d=(d+1)%4
        r = r+di[d]
        c = c+dj[d]


for x in arr:
    print(x)
