import sys
sys.stdin = open('input.txt','r')

N=int(input())
for _ in range(N):
    A,B = input().split(',')
    print(int(A)+int(B))