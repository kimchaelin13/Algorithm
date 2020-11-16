



di=[0,-1,0,1]
dj=[1,0,-1,0]

N=7
arr=[[0]*N for _ in range(N)]

num=N*N
i = N - 1
j = 0
d = 0

while True:

    if num == 0:
        break

    arr[i][j]=num

    num-=1

    ni=i+di[d]
    nj=j+dj[d]
    if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
        arr[ni][nj]=num
        i = ni
        j = nj
    else:
        d = (d+1)%4
        i += di[d]
        j += dj[d]


for x in arr:
    print(x)