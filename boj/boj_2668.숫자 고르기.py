'''
set을 이용해야할것같음

[ [],[],[],[] ,, ] 2차원리스트 만들어서
인덱스 1: 3, 이런식으로 함(길이는 n+1)

[[],[3],[1],[1],[5],[5],[4],[6]]

7
3
1
1
5
5
4
6

#1.출발한 인덱스번호 자기자신으로 돌아오면, 그 인덱스 번호를 출력
#2. 방문배열 만듦 [0]*(N+1)
#3.내가 만들 프로그램은 cnt_num(1)으로 출발하면, 1을 선택해야하는지 말아야하는지를 보고, 선택해야면 cnt+=1,아니면 cnt=0
'''

import sys
sys.stdin=open('input.txt','r')
from collections import deque

def cnt_num(v):
    Q=deque()
    Q.append(v)

    while Q:
        pv=Q.popleft()
        for i in linked[pv]:


N=int(input())
linked=[[] for _ in range(N+1)]
for i in range(1,N+1):
    linked[i].append(int(input()))
#print(linked)
check=[0]*(N+1)
for i in range(1,N+1):
    cnt_num(i)