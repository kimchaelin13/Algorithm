import sys
sys.stdin = open("input.txt", "r")

'''
사다리문제,도착지점이 2임. 그러면 2가 어디있는지 먼저 좌표값을 찾는다
그리고 거기서 DFS를 보내버리는거임

'''
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        #왼쪽
        if y-1 > 0 and maze[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x,y-1)
        #오른쪽
        elif y+1<10 and maze[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x,y+1)
        else:
            DFS(x-1,y)


if __name__=='__main__':
    maze=[list(map(int,input().split())) for _ in range(10)]
    ch=[[0]*10 for _ in range(10)]
    for y in range(10):
        if maze[9][y]==2:
            DFS(9,y)

