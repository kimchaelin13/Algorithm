import sys
sys.stdin=open('input.txt','r')


'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

#1.총 9명, 입력받음 
#2.무향그래프, 인접리스트 만듦
#3.bfs(7) 으로 시작해서 dist만듦/3이나 7이나 똑같은거아닌가?
#4.내가 만들 촌수계산 프로그램은 dist를 완성시켜서 거리계산해주는 프로그램
#5.dist[3]을 출력함
'''
from collections import deque
def family_dis(v):
    Q=deque()
    Q.append(v)

    while Q:
        pv=Q.popleft()
        for x in fr[pv]:
            if dist[x]==0:
                dist[x]=dist[pv]+1
                Q.append(x)
N=int(input())
P,C=map(int,input().split())
fr=[[]*(N+1) for _ in range(N+1)]
dist=[0]*(N+1)
for _ in range(int(input())):
    a,b=map(int,input().split())
    fr[a].append(b)
    fr[b].append(a)
family_dis(P)

#출력
flag=0 #정상
if dist[C]==0:
    flag=1

if flag==0:
    print(dist[C])
else:
    print(-1)