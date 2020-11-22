import sys
sys.stdin=open('input.txt','r')

for tc in range(1,int(input())+1):
    N,K=map(int,input().split())

    print('#{} {}'.format(tc, N%K))