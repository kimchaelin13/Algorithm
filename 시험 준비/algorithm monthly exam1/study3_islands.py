import sys
sys.stdin = open("input.txt", "r")

di=[0,0,1,-1,-1,1,-1,1] #우좌하상 우상대 우하대 좌상대 좌하대
dj=[1,-1,0,0,1,1,-1,-1]

def DFS(i,j):
    visited[i][j]=True
    # print(i,j)
    for d in range(8):
        ni=i+di[d]
        nj=j+dj[d]

        if ni<0 or ni>=N or nj<0 or nj>=N:
            continue
        if island_list[ni][nj]==False:
            continue
        if visited[ni][nj]==True:
            continue

        DFS(ni,nj)


for tc in range(1,int(input())+1):
    N=int(input())
    island_list=[list(map(int,list(input().split()))) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    num=0 #이건 테스트케이스가 달라질때마다 초기화를 시켜야하니까!!

    #island_list를 돌면서, 만약에 값이 들어있고, 또 visited에는 0이 있으면,
    #그건 그때 새로운 뭉텅이의 첫째 값이 진입했다는 것이다.
    #그러면 나는 뭉텅이의 개수를 구하는 것이기 때문에 num에 +1을 해주고
    #그 주위를 탐색하면서, 조건에 맞는데까지 계속 돌리면서!!

    for i in range(N):
        for j in range(N):
            if island_list[i][j] and visited[i][j]==False:
                print('----')
                num+=1
                DFS(i,j)
    print('#{} {}'.format(tc,num))

