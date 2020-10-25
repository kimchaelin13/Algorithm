import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
#1. linked list 만들기(무향그래프)
#2. 한번 찍은 노드는 다시 안찍어야 하니까 방문배열에 체크하고
#3. BFS 내가 만들 함수는, 함수(1) => 연결되는 모든 노드를 cnt에 추가해서 cnt를 리턴한 함수를 만들거야
#4. 1로 시작하면, 함수를 실행할건데
    일단 visited[1] = 표시
    q를 만들고
    q에 1을 넣고,
    cnt=0(1빼고 세는거니까)
    
    while Q: 
        Q에 있는 걸 popleft=V
        그리고 그 인접리스트[V] 중에 하나하나씩 조건을 만족하면 추가
        VISITED에 표시하고
        CNT를 추가한다
        
    RETURN CNT
'''

def check(v):
    visited[v]=True
    Q=deque()
    Q.append(v)
    cnt=0

    while Q:
        v=Q.popleft()
        for i in linked[v]:
            if not visited[i]:
                Q.append(i)
                visited[i]=True
                cnt+=1
    return cnt

if __name__=='__main__':
    V=int(input())
    E=int(input())
    linked=[[]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a,b=map(int,input().split())
        linked[a].append(b)
        linked[b].append(a)
    visited=[False]*(V+1)
    print(check(1))



#
# def ch_virus(v):
#     visited[v]=1
#     Q=deque()
#     Q.append(v)
#     cnt=0
#
#     while Q:
#         x=Q.popleft()
#         for i in linked[x]:
#             if not visited[i]:
#                 visited[i]=True
#                 Q.append(i)
#                 cnt+=1
#     return cnt
#
#
# if __name__=='__main__':
#     V,E=int(input()),int(input())
#     visited=[False]*(V+1)
#     linked=[[]*(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         a,b=map(int,input().split())
#         linked[a].append(b)
#         linked[b].append(a)
#     #print(linked)
#     print(ch_virus(1))
#