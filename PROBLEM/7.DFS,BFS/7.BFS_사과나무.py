import sys
sys.stdin = open("input.txt", "r")
from collections import deque
'''
BFS로 하면 마름모가 된다?
'''

dx=[-1,0,1,0] #시계방향
dy=[0,1,0,-1]
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
check=[[0]*n for _ in range(n)]
sum=0
Q=deque()

check[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2,n//2))
L=0 #레벨은 0이다

while True:
    if L==n//2: #종착점! 레벨이 2가 왔을때, 1까지 퍼져나감
        break

    size=len(Q) #L이 1일때 사이즈는 1이다. size만큼 for문을 돌린다.
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if check[x][y]==0:
                sum+=a[x][y]
                check[x][y]=1
                Q.append((x,y))
    L+=1
    # print(L,size)
    # for x in check:
    #     print(x)
    # L += 1
print(sum)






# '''
# 이중배열로 입력을 받고,
#
# '''
#
# N=int(input())
# farm=[list(map(int,input().split())) for _ in range(N)]
# total=[]
#
# for i in range(N):
#     middle=N//2
#     if i<middle:
#         total.extend(farm[i][middle-i:middle+i+1])
#
#     elif i==middle:
#         total.extend(farm[i][:])
#     else:
#         total.extend(farm[i][i-middle:middle-i])
#
# print(sum(total))
