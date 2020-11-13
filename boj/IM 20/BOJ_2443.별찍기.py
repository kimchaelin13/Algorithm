import sys
sys.stdin=open('input.txt','r')

N=int(input())
for i in range(1,N+1)[::-1]:
    res=' '*(N-i)+'*'*((2*i)-1)
    print(res)