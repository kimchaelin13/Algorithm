import sys
sys.stdin=open('input.txt','r')

N,M=map(int,input().split())

num=1
for i in range(N):
    for j in range(M):
        print(num,end=" ")
        num+=1
    print()