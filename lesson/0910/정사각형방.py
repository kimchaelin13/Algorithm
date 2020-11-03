T=int(input())


dr=[-1,1,0,0]
dc=[0,0,-1,1]

def BFS(stR,stC):
    global ans_num,ans_dist

    queue=[(stR,stC)]
    cnt=0

    while queue:
        r,c=queue.pop(0)
        cnt+=1
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            #범위체크안함
            if arr[nr][nc] - arr[r][c]==1:
                queue.append((nr,nc))

    if cnt>=ans_dist:
        if cnt==ans_dist:
            ans_num=min(ans_num,arr[stR][stC])
        else:
            ans_num=arr[stR][stC]

        ans_dist=cnt


for tc in range(1,T+1):
    N=int(input())

    arr=[[0]*(N+2) for _ in range(N+2)]

    #띠를 두르자, 위에서 범위체크안하려고
    '''
    0000
    0120
    0340
    0000
    이렇게 하면 띠를 두른 효과를 낼것임
    '''

    for i in range(1,N+1):
        tmp=list(map(int,input().split()))
        for j in range(1,N+1):
            arr[j][i]=temp[j-1]

    ans_dist=0
    ans_num=0

    for i in range(1,N+1):
        for j in range(1,N+1):
            BFS(i,j)
    print('#{} {} {}'.format(tc,ans_num,ans_dist))
