import sys
sys.stdin = open("input.txt", "r")
from collections import deque


'''
5로 시작해서 14로 갈건데
가장 적게 이동하면서 갈 수 있는 방법을 구하는것임. -> BFS
-1,+1,+5를 할 수 있다.


'''

MAX=10000
ch=[0]*(MAX)
dis=[0]*(MAX)
n,m=map(int,input().split())
ch[n]=1 #방문했으니까 n넣고
dis[n]=0 #여기는 0, 출발노드
Q=deque()
Q.append(n)

while Q:
    now=Q.popleft()
    if now==m:
        break
    for next in (now-1,now+1,now+5):
        if 0<next<=MAX and ch[next]==0:
            Q.append(next)
            ch[next]=1
            dis[next]=dis[now]+1
print(dis[m])
