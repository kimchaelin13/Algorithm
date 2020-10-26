import sys
sys.stdin = open("input5.txt", "r")


def BFS(start):
    visited[start] = 1
    Q.append(start)

    while Q:
        start=Q.pop(0)

        for next in range(1,N+1):
            if G[start][next] and not visited[next]:
                visited[next]=1
                Q.append(next)
                distance[next]=distance[start]+1

    return


for tc in range(1,11):
    LEN,INIT=map(int,input().split())
    arr=list(map(int,input().split()))
    N=max(arr)
    G=[[0]*(N+1) for _ in range(N+1)]

    for i in range(LEN//2):
        s=arr[i*2]
        e=arr[(i*2)+1]
        G[s][e]=1

    Q=[]
    distance,visited=[0]*(N+1), [0]*(N+1)

    BFS(INIT)

    MAX=0
    for i in range(1,len(distance)):
        if MAX<= distance[i]:
            MAX=distance[i]
            index=i

    print('#{} {}'.format(tc,index))