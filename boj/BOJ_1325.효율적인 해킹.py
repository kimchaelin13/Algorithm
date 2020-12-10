import sys
sys.stdin=open('input.txt','r')
'''
왜 출력초과일까? ㅠ 9퍼센트에서 출력초과
'''
from collections import deque

def bfs(v):
    global cnt
    Q=deque()
    checked = [False] * (N + 1)
    Q.append(v)

    while Q:
        x=Q.popleft()
        cnt+=1
        if linked[x]:
            for i in linked[x]:
                if checked[i]==False:
                    Q.append(i)
                    checked[i]=True

N,M=map(int,input().split())
linked=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    linked[b].append(a)
#print(linked)
res=[0]*(N+1)
for i in range(1,N+1):
    cnt=0
    bfs(i)
    res[i] = cnt
MAX=max(res)
#print(res)
for j in range(1,N+1):
    if res[j]==MAX:
        print(j,end=" ")