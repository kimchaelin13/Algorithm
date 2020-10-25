import sys
sys.stdin=open('input.txt','r')

N=int(input())
nums=list(map(int,input().split()))
nums.insert(0,0)
dp=[0]*(N+1)

#다음에 다시
