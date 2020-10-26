import sys
from collections import deque
sys.stdin = open("input.txt", "r")

MAX=10000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
n,m=map(int,input().split())
ch[n]=1
dis[n]=0
Q=deque()
Q.append(n)

while Q:
    now=Q.popleft()
    if now==m:
        break
    for next in (now-1,now+1,now*2):
        if 0<=next<=MAX and ch[next]==0:
            Q.append(next)
            ch[next]=1
            dis[next]=dis[now]+1
print(dis[m])