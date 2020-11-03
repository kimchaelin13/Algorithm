#정점, 간선의 개수
#간선들,,,

def dfs(v):
    #방문체크
    #v의 인접한 정점중에서 방문안한 정점을 재귀호출
    visited[v]=1
    print(v,end="")
    for w in range(1,N+1):
        if G[v][w] == 1 and visited[w] ==0:
            dfs(w)


#정점, 간선
N,E = map(int,input().split())
#간선들
temp=list(map(input().split()))
#인접행렬
G = [[0]*(N+1) for _ in range(N+1)]
#방문체크
visited = [0]*(N+1)

#간선들 잘라서 인접행렬에 저장
for i in range(E):
    s,e=temp[2*i],temp[2*i+1]
    G[s][e] =1
    G[e][s] =1
dfs(1)