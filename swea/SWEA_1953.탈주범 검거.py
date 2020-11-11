import sys
sys.stdin=open('input.txt','r')

'''
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0

#1.3을 만나면 dist 배열에 양옆으로 +1, -1
#2. 그리고 오른쪽으로 가면서 1을 만나면 0이 아닌 곳이면, dist 배열에 상하좌우에 부모노드 +1 을 한다 
#3. 마지막에 완성된 dist배열중에 3(시간)보다 작은것만 카운트한다 



#1.Q에 시작점을 넣고 시작, dist[pi][pj]=1, 체크 표시
#2.(pi,pj)를 꺼낸다
#3.
    arr[pi][pj]==3이면, dist[pi][pj-1], dist[pi][pj+1]가 0이 아니고, 방문하지 않았다면 dist[pi][pj]+1로 표시
    arr[pi][pj]==1이면, dist[pi-1][pj], dist[pi+1][[pj], dist[pi][pj+1], dist[pi][pj-1] 에 dist[pi][pj]+1
    arr[pi][pj]==2이면, dist[pi-1][pj], dist[pi+1][pj] 
    arr[pi][pj]==4이면, dist[pi-1][pj], dist[pi][pj+1]
    arr[pi][pj]==5이면, dist[pi+1][pj], dist[pi][pj+1]
    arr[pi][pj]==6이면, dist[pi+1][pj], dist[pi][pj-1]
    arr[pi][pj]==7이면, dist[pi-1][pj], dist[pi][pj-1]
#4.그리고 



'''
from collections import deque
di=[-1,1,0,0] #상하좌우
dj=[0,0,-1,1]
info=[0,[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]

def make_dist(i,j):
    #check[i][j]=True
    Q=deque()
    dist[i][j]=1
    Q.append((i,j))

    while Q:
        pi,pj=Q.popleft()
        for d in info[arr[pi][pj]]:
            ni=pi+di[d]
            nj=pj+dj[d]
            if 0 <= ni < N and 0 <= nj < M and dist[ni][nj] == 0 and arr[ni][nj] != 0:
                if d==0 and (arr[ni][nj] not in [1,2,5,6]):
                    continue
                elif d==1 and (arr[ni][nj] not in [1,2,4,7]):
                    continue
                elif d==2 and (arr[ni][nj] not in [1,3,4,5]):
                    continue
                elif d==3 and (arr[ni][nj] not in [1,3,6,7]):
                    continue
                dist[ni][nj] = dist[pi][pj] + 1
                Q.append((ni, nj))

for tc in range(1,int(input())+1):
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dist=[[0]*M for _ in range(N)]
    #check=[[False]*M for _ in range(N)]
    make_dist(R,C)
    cnt=0
    for i in range(N):
        for j in range(M):
            if 0<dist[i][j] <= L:
                cnt+=1
    print('#{} {}'.format(tc,cnt))