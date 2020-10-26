import sys
sys.stdin = open("input.txt", "r")

di=[0,0,1,-1]
dj=[1,-1,0,0]

def DFS(i,j):
    global result
    visited[i][j]=1

    if board[i][j]==3:
        result=1
        return

   else:
        for d in range(4):
            ni=i+di[d]
            nj=j+dj[d]

            if ni<0 or ni>=16 or nj<0 or nj>=16:
                continue
            if visited[ni][nj]==True:
                continue
            if board[ni][nj]==1:
                continue
            DFS(ni,nj)



for tc in range(1,11):
    N=int(input())
    board=[list(map(int,list(input()))) for _ in range(16)]
    visited=[[0]*16 for _ in range(16)]
    result=0 #결과 초기화!! 테스트케이스마다
    for i in range(16):
        for j in range(16):
            DFS(1,1)

    print('#{} {}'.format(tc,result))