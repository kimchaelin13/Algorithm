#input
#정점수, 간선수
#7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7

def DFS(v):
    #노드에 가자마자 찍히니까 프린트하고
    print(v,end=" ")
    #방문값을 1로 만들고
    visited[v] = 1
    #GLOBAL을 사용하지않았는데도 V를 쓸 수 있는건 우리는 V를 수정하지 않고 그대로 이용하는것이기때문
    for i in range(1,V+1):
        #현재 내 정점 v와 연결되어 있는지 확인/그리고 아직 방문하지 않은곳일때
        if arr[v][i] ==1 and visited[i]==0 :
            DFS(i)


#입력 먼저
V,E = map(int,input().split())
#7칸이라고 하고 0으로 초기화된 7*7 칸 만든것!한칸 크게 만든것임 읽기 편할려고,인덱스 맞출려고!!
arr = [[0]*(V+1) for _ in range(V+1)]


#0으로 초기화된 보드를 만들고, 33번 코드로 인접행렬을 완성시킴
for i in range(E):
    st, ed = map(int,input().split())
    # since 무향 그래프, 서로 연결되있음을 표시
    arr[st][ed] = arr[ed][st] = 1


#정점,방문 표를 만드는거임(방문배열 선언)
visited=[0]*(V+1)

DFS(1)
