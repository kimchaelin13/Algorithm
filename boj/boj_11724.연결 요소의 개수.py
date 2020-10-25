import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
#1. 입력을 받고
#2. 연결리스트를 만들자
#3. 그러면 그 연결리스트를 돌면서, 안에 뭐가 있으면, 한 뭉탱이 찾은거니까, cnt+=1, cnt_link(i)
#4. 방문체크 미리 만들어서 그 노드는 다시 방문안하게 방문표시하고
#5. Q를 만들어서 그 i를 안에 Q에 넣음
#6. 그리고 while문을 돌리면서, Q에 있는 노드 꺼내서
#7. 연결리스트[현재노드]에 있는 i를 탐색하는데, 아직 방문하지 않았다면, 거기로 갈거임
    방문체크하고, Q에 넣음
'''
def cnt_link(v):
    visited.add(v)
    Q=deque()
    Q.append(v)

    while Q:
        pn=Q.popleft()
        for k in linked[pn]:
            if k not in visited:
                Q.append(k)
                visited.add(k)


V,E=map(int,sys.stdin.readline().split())
linked=[[]*(V+1) for _ in range(V+1)]
#visited=[False]*(V+1)
visited=set()
for _ in range(E):
    a,b=map(int,sys.stdin.readline().split())
    linked[a].append(b)
    linked[b].append(a)
cnt=0
for i in range(1,V+1):
    if linked[i] !=0 and i not in visited:
        cnt+=1
        cnt_link(i)
print(cnt)

# def bfs(v):
#     visited[v]=True
#     Q=deque()
#     Q.append(v)
#     cnt=0
#
#     while Q:
#         x=Q.popleft()
#         for i in linked[x]:
#             if not visited[i]:
#                 visited[i]=True
#                 Q.append(i)
#                 cnt+=1
#     return cnt
#
# V,E=map(int,input().split())
# linked=[[]*(V+1) for _ in range(V+1)]
# visited=[False*(V+1) for _ in range(V+1)]
# for _ in range(E):
#     a,b=map(int,input().split())
#     linked[a].append(b)
#     linked[b].append(a)
#
# print(bfs(1))


# import sys
#
# sys.setrecursionlimit(10000)
#
#
# def dfs(v):
#     visited[v] = True
#     for e in adj[v]:
#         if not visited[e]:
#             dfs(e)
#
#
# N, M = map(int, input().split())
# adj = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1)
# count = 0
#
# for _ in range(M):
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)
#
# for j in range(1, N + 1):
#     if not visited[j]:
#         dfs(j)
#         count += 1
#
# print(count)