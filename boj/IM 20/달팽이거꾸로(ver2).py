import sys
sys.stdin=open('input.txt','r')

di=[0,-1,0,1]
dj=[-1,0,1,0]

N=5
arr=[[0]*N for _ in range(N)]

i=N//2
j=N//2
d=0
num=1
size=1

while True:
    arr[i][j]=num

    while size:
        ni = i +di[d]
        nj = j +dj[d]


