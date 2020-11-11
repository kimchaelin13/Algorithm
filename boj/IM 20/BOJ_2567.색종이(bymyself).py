import sys
sys.stdin=open('input.txt','r')
'''
둘레 문제다. 어떤 1을 세야 하냐면, 주변이 0이 하나라도 있을때(테두리1이라는뜻임),
                              또는 벽에 붙어있을때(좌표라서 범위밖에 있을때(0보다 작거나, 99보다 크거나)
4
3 7
5 2
15 7
13 14
'''
di=[-1,0,1,0]
dj=[0,1,0,-1]
def check(i,j):
    global ans

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]
        #코드 줄이기
        #아예 101개를 만들어서 0번째에 걸리거나, 맨 마지막 100까지 범위를 포함함
        #좌표이기 때문임
        if 0<=ni<101 and 0<=nj<101:
            if arr[ni][nj]==0:
                ans+=1

arr=[[0]*101 for _ in range(101)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    for r in range(x,x+10):
        for c in range(y,y+10):
            arr[r][c]=1
ans=0
for i in range(101):
    for j in range(101):
        if arr[i][j]==1:
            check(i,j)
print(ans)
