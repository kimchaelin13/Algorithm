import sys
sys.stdin = open("input.txt", "r")
############dfs로 풀기##################
# def DFS(v):
#     visited[v]=1
#     for i in range(N+1):
#         if arr[v][i]==1 and visited[i]==0:
#             DFS(i)
#
# for tc in range(1,int(input())+1):
#     N,M=map(int,input().split())
#     arr=[[0]*(N+1) for _ in range(N+1)]
#     visited=[0 for _ in range(N+1)]
#     cnt = 0
#     #연결된마을 행렬 완성
#     for _ in range(M):
#         st,ed=map(int,input().split())
#         arr[st][ed]=arr[ed][st]=1
#
#     for i in range(1,N+1):
#         if not visited[i]:
#             DFS(i)
#             cnt+=1
#     print('#{} {}'.format(tc,cnt))

#########bfs로 풀기##########

def bfs(v):
    visited[v] = 1
    q.append(v)
    while q:
        a = q.pop(0)
        for j in arr[a]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    #print(arr)
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    print(arr)
    visited = [0] * (N + 1)
    q = []
    cnt = 0
    for n in range(1, N + 1):
        if not visited[n]:
            cnt += 1
            bfs(n)
    print("#{} {}".format(test_case, cnt))