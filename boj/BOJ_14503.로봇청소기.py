import sys
sys.stdin=open('input.txt','r')

'''
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

'''
di=[-1,0,1,0] #븍 동 남 서
dj=[0,1,0,-1]

d_L=[3,0,1,2]
d_B=[2,3,0,1]

def recur(i,j,dir,end):
    global cnt
    if arr[i][j]==0:
        cnt+=1
        checked[i][j]=True

    cur_L = d_L[dir]
    ni = i+di[cur_L]
    nj = j+dj[cur_L]
    #왼쪽 방향에 아직 청소하지 않았고, 방문도 안했으면
    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and checked[ni][nj]==False:
        recur(ni,nj,cur_L,end)
    #왼쪽방향인데 이미 방문해서 청소했음
    elif 0<=ni<N and 0<=nj<M and checked[ni][nj]==True:
        recur(i,j,cur_L,end+1)
    else:
        if end!=4:
            cur_B = d_B[dir]
            bi = i+di[cur_B]
            bj = j+dj[cur_B]
            if 0<=ni<N and 0<=nj<M and checked[ni][nj]==False:
                recur(bi,bj,dir,end)

        else:
            return






N,M=map(int,input().split())
i,j,dir = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
checked = [[False]*M for _ in range(N)]
cnt=0
recur(i,j,dir,0)