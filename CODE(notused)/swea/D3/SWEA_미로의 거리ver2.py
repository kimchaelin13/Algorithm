import sys
sys.stdin=open('input.txt','r')






tc=int(input())

for
n=int(input())
maze=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maze[i][j]==2:
            check()
