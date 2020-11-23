import sys
sys.stdin=open('input.txt','r')



def check_sosu(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

N=int(input())
nums = list(map(int,input().split()))
ans=0
for i in range(N):
    ans += check_sosu(nums[i])
print(ans)
