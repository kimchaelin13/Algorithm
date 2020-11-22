import sys
sys.stdin=open('input.txt','r')

N,M=map(int,input().split()) #n이 행이고,m이 열이다

chess = [list(input()) for _ in range(N)]
print(chess)
