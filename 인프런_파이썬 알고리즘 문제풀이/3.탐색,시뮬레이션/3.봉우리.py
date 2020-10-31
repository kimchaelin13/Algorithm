import sys
sys.stdin=open('input.txt','r')
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
#가장자리 다 0으로 만드는 방법
a.insert(0,[0]*n) #맨위 행
a.append([0]*n) #맨아래행
for x in a:
    x.insert(0,0)
    x.append(0)
cnt=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         #all은 그 안에 조건이 모두가 참일때 참
#         if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt+=1
# print(cnt)


