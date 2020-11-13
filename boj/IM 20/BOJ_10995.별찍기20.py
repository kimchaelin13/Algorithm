import sys
sys.stdin=open('input.txt','r')

N=int(input())
a,b='* ',' *'

for i in range(N):
    if i==0 or i%2==0:
        print(a*N)
    else:
        print(b*N)
