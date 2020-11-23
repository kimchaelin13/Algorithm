import sys
sys.stdin=open('input.txt','r')

A,B=map(int,input().split())

M = min(A,B)
MAX = 0
for i in range(1,M+1):
    if (A%i==0) and (B%i==0):
        if i>MAX:
            MAX = i
print(MAX)
print((A//MAX) * (B//MAX)*MAX)