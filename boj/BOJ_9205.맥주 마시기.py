import sys
sys.stdin=open('input.txt','r')

'''
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000

from collections import deque
def bfs():
    Q=deque()
    Q.append(info[0])
    visited[0]=True

    while Q:
        p_x,p_y = Q.popleft()
        if p_x == info[-1][0] and p_y == info[-1][1]:
            return 'happy'
        for idx,(n_x,n_y) in enumerate(info):
            if not visited[idx] and abs(p_x-n_x) + abs(p_y-n_y)<=50*20:
                Q.append((n_x,n_y))
                visited[idx]=True
    return 'sad'

for tc in range(int(input())):
    N=int(input())
    info=[]
    visited = [False]*(N+2)
    for _ in range(N+2):
        a,b=map(int,input().split())
        info.append((a,b))
    print(bfs())


플로이드-와샬 이건뭘까

max = 1000

t = int(input())
for _ in range(t):
    n = int(input())
    homeX, homeY = map(int, input().split())
    stores = []
    for _ in range(n):
        storeX, storeY = map(int, input().split())
        stores.append((storeX, storeY))
    festivalX, festivalY = map(int, input().split())

    graph = [[max] * (n + 2) for _ in range(n + 2)]
    arr = [(homeX, homeY)]
    arr.extend(stores)
    arr.append((festivalX, festivalY))

    # 정점 간 이동 가능 표시
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                graph[i][j] = 0
                continue
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            if dist <= 1000:
                graph[i][j] = 1

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    if 0 < graph[0][n +1] < max:
        print('happy')
    else:
        print('sad')
'''



# 이거 왜 안돼?
def isPossible(pre):
    global flag
    #pre가 페스티벌 좌표이면 return
    if pre == info[-1]:
        return
    if abs(pre[0] - info[-1][0]) + abs(pre[1] - info[-1][1]) <=1000:
        return

    MIN=987654321
    #1번 편의점부터 페스티벌 좌표까지 돌면서
    for d in range(1,N+2):
        #아직 방문하지 않은 곳이라면
        if visited[d]==False:
            #거리를 구해서
            temp = abs(pre[0] - info[d][0]) + abs(pre[1] - info[d][1])
            #거리의 최솟값을 구한다.
            if MIN > temp:
                MIN = temp
                next = info[d]
    if 20*50 < MIN:
        flag=1
    else:
        visited[info.index(next)] = True
        isPossible(next)

for tc in range(int(input())):
    flag=True
    N=int(input())
    flag=0
    info=[]
    for i in range(N+2):
        x,y=map(int,input().split())
        info.append((x,y))
    #(0,0)에서 출발하니까, 시작점은 True로 미리 처리
    visited = [True] + [False]*(N+1)
    pre = info[0]
    # (0,0)일때 가장 가까운 좌표를 구하고, 거기까지 갈때 20*50안에 갈수있는지
    isPossible(pre)
    if flag:
        print('sad')
    else:
        print('happy')
