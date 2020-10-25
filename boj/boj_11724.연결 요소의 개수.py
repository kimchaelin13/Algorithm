import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
#Q를 씀 - 왜냐면, 그 요소 안에 얼마나 들어있는지 모름
#갈때가 없으면 함수 아래로 내려가징낳나? 그때 CNT를 1추가
'''

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


import sys

sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)