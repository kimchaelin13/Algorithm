import sys
sys.stdin=open('input.txt','r')

'''
6
5
1 2
1 3
3 4
2 3
4 5

#1.입력받고, 양방향 리스트를 만듦.

#2.cnt_invite(1)로 출발
    이 프로그램은 친구 한명한명당 상근이와 얼마나 떨어져있는지 distanct를 계산해줌
    => dist[] 있어야함
#3.그리고 프로그램 끝나면 dist에 다 추가 되있어야 함. dist의 value가 2인것만그 개수를 세줌
'''
from collections import deque
def fd(v):
    Q=deque()
    Q.append(v)

    while Q:
        pv=Q.popleft()
        for x in fr[pv]:
            if dist[x]==0:
                dist[x]=dist[pv]+1
                Q.append(x)
N=int(input())
M=int(input())
fr=[[]*(N+1) for _ in range(N+1)]
dist=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    fr[a].append(b)
    fr[b].append(a)
fd(1)

#출력
cnt=0
for i in range(2,N+1):
    if dist[i]!=0 and dist[i]<=2:
        cnt+=1
print(cnt)