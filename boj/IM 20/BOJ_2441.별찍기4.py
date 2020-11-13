import sys
sys.stdin=open('input.txt','r')

N=int(input())
for i in range(N):
    print(' '*i+(N-i)*'*')