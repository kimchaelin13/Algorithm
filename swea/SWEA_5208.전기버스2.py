import sys
sys.stdin=open('input.txt','r')
'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''
def dfs(L,cnt):
    global MIN
    # if total+(sum(capacity)-tsum) < busstop:
    #     return
    # print(L,cnt)
    if MIN<cnt:
        return
    if L>=len(capacity):
        if MIN>cnt:
            MIN=cnt
            # print('MIN',MIN)
    else:
        for x in range(L+1,L+capacity[L]+1)[::-1]:
            if x>len(capacity):
                continue
            dfs(x,cnt+1)


for tc in range(1,int(input())+1):
    temp=list(map(int,input().split()))
    busstop=temp[0]
    capacity=temp[1:]
    # print(capacity)
    MIN=987654321
    dfs(0,0)
    print('#{} {}'.format(tc,MIN-1))

# def dfs(L,cnt):
#     global MIN
#     # if total+(sum(capacity)-tsum) < busstop:
#     #     return
#     if MIN<cnt:
#         return
#     if L==len(capacity):
#         if MIN>cnt:
#             MIN=cnt
#     else:
#         for x in range(L+1,L+capacity[L]+1)[::-1]:
#             if x>len(capacity):
#                 continue
#             dfs(x,cnt+1)
#             dfs(x,cnt)
#
# for tc in range(1,int(input())+1):
#     temp=list(map(int,input().split()))
#     busstop=temp[0]
#     capacity=temp[1:]
#     print(capacity)
#     MIN=987654321
#     dfs(0,0)
#     print('#{} {}'.format(tc,MIN-1))








'''
from collections import deque
def bfs(V):
    Q=deque()
    Q.append(V)

    while Q:
        x=Q.popleft()
        for i in linked[x]:
            # print('x',x,i)
            if i==busstop+1:
                return
            if dist[i]==0:
                dist[i]=dist[x]+1
                Q.append(i)


for tc in range(1,int(input())+1):
    temp=list(map(int,input().split()))
    busstop=temp[0]
    capacity=temp[1:]+[0]
    #print(capacity)
    linked=[[] for _ in range(busstop+1)]
    for i in range(1,len(capacity)+1):
        linked[i].extend(list(x for x in range(i+1,i+capacity[i-1]+1)))
    # print(busstop,linked)
    dist=[0]*(busstop+1)
    bfs(1)
    # print(dist)
    print('#{} {}'.format(tc,dist[busstop]-1))
'''