import sys
sys.stdin = open("input1.txt", "r")

'''
bfs와 queue 활용
방향성이 없다. [start][end] [end][start]모두 체크

'''

def BFS(startN):
    global result
    Q.append(startN)
    visited[startN]=1

    while Q:
        startN=Q.pop(0)

        for i in range(1,V+1):
            if arr[startN][i] and not visited[i]:
                Q.append(i)
                visited[i]=1
                distance[i]=distance[startN]+1
                if i == EndN:
                    result=distance[i]
                    return


for tc in range(1,int(input())+1):
    V,E=map(int,input().split())
    arr=[[0]*(V+1) for _ in range(V+1)]
    visited=[0]*(V+1)
    distance=[0]*(V+1)

    for i in range(E):
        s,e=map(int,input().split())
        arr[s][e], arr[e][s]=1,1

    startN, EndN = map(int,input().split())

    Q=[]
    result=0
    BFS(startN)
    print('#{} {}'.format(tc,result))
