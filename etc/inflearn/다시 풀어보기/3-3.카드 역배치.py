import sys
sys.stdin=open('input.txt','r')

nums=list(range(21))
c=1
for _ in range(10):
    s,e=map(int,input().split())
    for i in range((e-s+1)//2):
        nums[s+i],nums[e-i]=nums[e-i],nums[s+i]
nums.pop(0)
print(*nums)
# a=list(range(21))
#
# for _ in range(10):
#     s,e=map(int,input().split())
#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i] = a[e-i], a[s+i]
# a.pop(0)
# for x in a:
#     print(x,end=' ')