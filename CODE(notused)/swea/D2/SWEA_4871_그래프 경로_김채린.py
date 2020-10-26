import sys
sys.stdin = open("input.txt", "r")

'''
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
 

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
 

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

#우선 입력을 먼저 받자, 내가 필요한건 간선간의 관계를 알려주는 2차원 배열이 필요하고 또 visited 1차원 배열이 필요하다


'''
def DFS(s):
    visited[s] = 1
    #

    for w in range(1,V+1):
        if G[s][w] == 1 and visited[w]==0:
            DFS(w) #가라고 시킨다, 뭐래 ㅠㅠ


for tc in range(1,int(input())+1):
    V,E=map(int,input().split())
    G=[[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        u,v=map(int,input().split())
        #유향이니까 반대는 표시하지 않기
        G[u][v]=1
    s,e = map(int,input().split())
    visited=[0]*(V+1) #호출하기 전에 이것도 만들어야함
    DFS(s) #호출하자, 갈수있는데를 다 가라고 시켜야함
    print('#{} {}'.format(tc,visited[e])) #출발점을 s로 주고 돌렸을때, 경로가 있다면 방문표시가 되었을것이다. ?엥,,,ㅋ
