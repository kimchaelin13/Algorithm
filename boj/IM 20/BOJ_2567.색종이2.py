import sys
sys.stdin=open('input.txt','r')

'''
100*100 배열 만들고,
색종이 개수만큼 돌면서
    a,b받고
    x,y,xx1,yy1=a,b,a+10,b+10
    그리고 for (x1,xx1):
            for (y1,yy1):
                arr[r][c]=1
    
벽으로 둘러쌓여있거나, 0으로 둘러쌓여있을때 => 둘레길이를 구할 수 있다.
arr[r][c]를 돌면서 만약에 그 값이 1인데, 상하좌우 돌면서 그 중에 하나라도 0이라면, +1을 한다.
'''
from collections import deque
di=[-1,1,0,0]
dj=[0,0,-1,1]
#1을 만나면 거기가 겉에 있는 곳인지 체크해줄 함수(0이거나 벽이면 거기가 겉에있는 곳임)
def check(i,j):
    global res
    Q=deque()
    Q.append((i,j))

    while Q:
        pi,pj=Q.popleft()
        for d in range(4):
            ni=pi+di[d]
            nj=pj+dj[d]
            #테두리에 걸려있을떼
            if ni<0 or ni>=100 or nj<0 or nj>=100:
                res+=1
            #주변에 0이 있으면
            elif arr[ni][nj]==0:
                res+=1

arr=[[0]*100 for _ in range(100)]
#ch=[[False]*100 for _ in range(100)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    x,y,xx,yy=a,b,a+10,b+10
    for i in range(x,xx):
        for j in range(y,yy):
            arr[i][j]=1

res=0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1:
            #만약에 1을 만나면 그 1이 가장 겉에있는 1인지 체크해줌
            check(i,j)
print(res)