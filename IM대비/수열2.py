import sys
sys.stdin=open('input.txt','r')

N,K=map(int,input().split())
nums=list(map(int,input().split()))

res=0
for i in range(0,N):
    tmp=0
    tmp += sum(nums[i:i+K])

    if tmp>res:
        res=tmp
print(res)