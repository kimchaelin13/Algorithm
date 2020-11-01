##BFS로 풀면?###
def BFS(v):
    queue = [v]
    visited[v] = 1

    while queue:
        #큐에서 한명 꺼내기
        curr = queue.pop(0)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


##dfs로 풀면?####

def DFS(v):
    visited[v]=1

    for i in adj[v]:
        if not visited[i]:
            DFS(i)

T=int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    #인접리스트
    adj = [[] for _ in range(V+1)]

    for i in range(E):
        A, B = map(int, input().split())
        adj[A].append(B)
        adj[B].append(A)

    visited = [0] * (V+1)

    ans = 0

    for i in range(1, V+1):
        if visited[i] == 0:
            ans+=1
            BFS(i)

    print("#{} {}".format(tc, ans))