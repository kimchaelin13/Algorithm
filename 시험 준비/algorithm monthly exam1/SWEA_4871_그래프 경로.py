import sys
sys.stdin = open("input.txt", "r")

def DFS(s):
    global result
    visited[s]=1



    for i in range(E):
        if arr[s][i]==1 and visited[i]==0:
            if i == e:
                result=1
                return result
            DFS(i)




for tc in range(1,int(input())+1):
    V,E=map(int,input().split())
    arr=[[0]*(V+1) for _ in range(V+1)]
    visited=[0]*(V+1)

    for i in range(E):
        u,v=map(int,input().split)
        arr[u][v]=1
    s,e=map(int,input().split())
    result=0
    DFS(s)




