import sys
sys.stdin=open('input.txt','r')

N=int(input())

# s=N
# for _ in range(N):
#     print(s*'*')
#     s-=1
#

for i in range(N+1)[::-1]:
    print(i*'*')