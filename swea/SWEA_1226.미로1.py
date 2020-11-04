import sys
sys.stdin=open('input (49).txt','r')

'''

'''
di=[0,1,0,-1]
dj=[1,0,-1,0]
def dfs(i,j):
    global ans
    # check[i][j]=True

    if arr[i][j]==3:
        ans=1
        return
    else:
        for d in range(4):
            ni=i+di[d]
            nj=j+dj[d]
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj]==0 and check[ni][nj]==False:
                check[ni][nj]=True
                dfs(ni,nj)
                check[ni][nj]=False

for tc in range(1,11):
    t=int(input())
    arr=[list(map(int,input())) for _ in range(16)]
    check=[[False]*16 for _ in range(16)]
    #print(arr)
    ans=0
    dfs(1,1)
    print('#{} {}'.format(tc,ans))