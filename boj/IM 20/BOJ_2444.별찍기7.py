import sys
sys.stdin=open('input.txt','r')

N=int(input())

# for i in range(N):
#     print(' '*(N-(i+1))+'*'*((2*i)+1))

for i in range(2*(N-1)+1):
    if i>(N-1):
        i=(2*N-2)-i
    print(' '*(N-(i+1))+'*'*((2*i)+1))