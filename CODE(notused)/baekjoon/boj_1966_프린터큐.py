import sys
sys.stdin = open("input.txt", "r")
from collections import deque
'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    Q=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
    #Q=[(0,1),(1,2),(2,3),(3,4)] 이런식으로 만듦

    Q=deque(Q)
    cnt=0

    while True:
        cur=Q.popleft()
        if any(cur[1]<x[1] for x in Q):
            Q.append(cur)
        else:
            cnt+=1
            if cur[0] == M:
                print(cnt)
                break



