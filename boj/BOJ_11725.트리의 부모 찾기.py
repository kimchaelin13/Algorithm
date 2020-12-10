
import sys
sys.stdin=open('input.txt','r')

N=int(input())
linked=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    linked[a].append(b)
    linked[b].append(a)

print(linked)