import sys
sys.stdin=open('input.txt','r')

'''
5
54321



'''
N=int(input())
nums=int(input())
res=0
# N만큼 돌면서
for i in range(N):
    res += nums%10
    nums = nums//10

print(res)

print(ord('z'))