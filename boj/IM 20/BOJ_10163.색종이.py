import sys
sys.stdin=open('input.txt','r')

'''
101 * 101

0 0 10 10
2 2 6 6

'''


arr= [[0]*101 for _ in range(101)]
N=int(input())
num=1
for _ in range(N):
    r,c,n,m=map(int,input().split())

    for i in range(r,r+n):
        for j in range(c,c+m):
            arr[i][j] = num
    num+=1

res = []
for k in range(1,N+1):
    total = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j]==k:
                total += 1
    res.append(total)

for r in res:
    print(r)