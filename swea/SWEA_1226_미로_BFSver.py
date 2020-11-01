import sys
sys.stdin = open("input.txt", "r"
)

def BFS(i,j):
    global result
    queue=[]
    queue.append(maze[i][j])

    visited[i][j]=1

    while len(queue)>0:
        curr=queue.pop(0)
        print(curr,end= " ")

        for i in










for tc in range(1,11):
    N=int(input())
    maze=[list(map(int,list(input()))) for _ in range(16)]
    visited=[[0]*16 for _ in range(16)]
    result=0
    for i in range(16):
        for j in range(16):
            if maze[i][j] != 0 and visited[i][j]==Fasle:
                DFS(1,1)