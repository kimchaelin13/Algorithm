import sys
from collections import deque
sys.stdin=open('input.txt','r')

'''
#인접리스트/유향 그래프

#1. 학생수+1 길이만큼 [ [] [] [] [] []] 이런식으로 만듦
#2. 문제처럼 채워넣음
#3. bfs로 풀것
    cnt_team(1)
#4. 내가 만들 프로그램은 출발하게 했을때,그 프로그램에서
    함께 하는 팀 인원수를 모두 세줄것임

#5. 그리고 그 팀이 된 cnt를 저장해서 [1,3,,]저장함
#6. 그리고 출력은 인원수-sum(res) 로
'''
def cnt_team(v):
    global cnt
    Q=deque()
    Q.append(v)
    #visited[v]=True

    while Q:
        x=Q.popleft()
        for i in choose[x]:
            #i도 x를 선택해야함
            if not visited[i]:
                cnt+=1
                Q.append(i)
    res.append(cnt)

for tc in range(1,int(input())+1):
    N=int(input())
    choose=[[]*(N+1) for _ in range(N+1)]
    visited=[False]*(N+1)

    temp=list(map(int,input().split()))
    temp.insert(0,0)
    for i in range(1,N+1):
        choose[i].append(temp[i])
    #print(choose)
    res=[]
    cnt=0
    for i in range(1,N+1):
        cnt_team(i)
    print(res)