import sys
sys.stdin=open('input.txt','r')


'''
2
6 5
2 3
3 4
4 5
5 6
2 5
6 5
1 2
1 3
3 4
2 3
4 5

'''
from collections import deque
def invite(V):
    Q=deque()
    Q.append(V)

    while Q:
        x=Q.popleft()
        for j in fr[x]:
            if dist[j]==0:
                dist[j]=dist[x]+1
                Q.append(j)

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    fr=[[] for _ in range(N+1)]
    #print(fr)
    for _ in range(M):
        a,b=map(int,input().split())
        fr[a].append(b)
        fr[b].append(a)

    dist=[0]*(N+1)
    #print(fr)
    invite(1)
    #print(dist)
    #출력
    cnt=0
    for i in dist:
        if i!=0 and i<=2:
            cnt+=1
    if cnt==0:
        print('#{} {}'.format(tc,cnt))
    else:
        print('#{} {}'.format(tc,cnt-1))