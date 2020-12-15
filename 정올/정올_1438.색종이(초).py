import sys
sys.stdin=open('input.txt','r')

arr=[[0]*100 for _ in range(100)]

for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j] = 1


cnt=0
for r in range(100):
    for c in range(100):
        if arr[r][c]==1:
            cnt+=1
print(cnt)