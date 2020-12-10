import sys
sys.stdin=open('input.txt','r')

from collections import deque
def dfs(v):
    print(v,end=" ")
    checked[v]=True
    if linked[v]:
        for i in linked[v]:
            if checked[i]==False:
                checked[i]=True
                dfs(i)
def bfs(v):
    # print(v,end=" ")
    Q=deque()
    Q.append(v)
    checked_1[v]=True
    while Q:
        x=Q.popleft()
        print(x,end=" ")
        if linked[x]:
            for j in linked[x]:
                if checked_1[j]==False:
                    checked_1[j] = True
                    Q.append(j)

N,M,V=map(int,input().split())
linked = [[] for _ in range(N+1)]
checked = [False]*(N+1)
checked_1 = [False]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    linked[a].append(b)
    linked[b].append(a)
for x in linked:
    x.sort()
dfs(V)
print()
bfs(V)
