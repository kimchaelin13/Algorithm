import sys
sys.stdin=open('input.txt','r')

N=int(input())

for i in range(N):
    if i==0:
        print(' ' * (N - (i + 1)) + '*' * 1 + ' ' * (2 * i - 1) + '*' * 0)
    else:
        print(' '*(N-(i+1))+'*'*1+' '*(2*i-1)+'*'*1)