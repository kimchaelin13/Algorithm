'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
오잉 이거 답이 틀렸움 @ 코드 다시 봐야돼!
'''
def bfs(v):
    #큐,방문
    Q=[]
    visit=[0]*(V+1)

    #enQ(v),visited(v)
    Q.append(v)
    visit[v]=1
    print(v,end=" ")
    #큐가 비어있지 않는 동안
    while Q:
        #v=deQ()
        v=Q.pop(0)
        #v의 인접한 정점(w)증에서 방문안한 정점이면
        for w in range(1,V+1):
            if G[v][w]==1 and visit[w]==0:
            #enQ(w), 방문처리(v)
                Q.append(w)
                visit[w]=1
                print(v,end=" ")



#입력 -> 인접행렬
V,E = map(int,input().split())
temp = list(map(int,input().split()))
#인접행렬 초기화
G=[[0]*(V+1) for _ in range(V+1)]
#인접행렬 저장
for i in range(E): #이게머임
    s,e=temp[2*i],temp[2*i+1]
    G[s][e]=G[e][s]=1
#인접행렬 출력
for i in range(1,V+1):
    print("{} {}".format(i,G[i]))

bfs(1)