import sys
sys.stdin=open('input.txt','r')

N=int(input())

for i in range(2*N-1):
    if i>=N:
        i=(2*N-2)-i
    print(' '*(N-(i+1))+'*'*(i+1))