dr=[-1,1,0,0]
dx=[0,0,-1,-1]
#사방탐색으로 행렬을 준다
'''
2차원 dfs를 이용해서 ! 1을 세기

이게 입력임
7
0000000
0000000
0011100
0010111
0110010
0011100
0000000
'''
def DFS(r,c):
    #카운트 개수세야하니까 선언
    global cnt
    #요기 왔다는건 1이라는 뜻이니까 카운트증가
    arr[r][c]=0
    cnt+=1

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        #수행할필여없으니까 컨티뉴뉴
       if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        #
        if arr[nr][nc]==0:
            continue
        DFS(nr,nc)

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)] #2차원 리스트 완성

#2차원 순회하면서 1인 좌표부터 찾음
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            #ㄱ개수 세야되니까 새로 세야하기 때문에 초기화
            cnt=0
            DFS(i,j) #??
            print(cnt) #