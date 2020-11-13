import sys
sys.stdin=open('input.txt','r')

N=int(input())
s='* '
for i in range(N):
    print(' '*(N-(i+1))+s*(i+1))