import sys
sys.stdin=open('input.txt','r')

#DP로 풀어야지
N=int(input())
dp=[0]*N
nums=list(map(int,input().split()))

for k in range(N):
    if k==0:
        dp[k] = nums[k]
    else:
        if nums[k] > nums[k] + dp[k-1]:
            dp[k] = nums[k]
        else:
            dp[k] = nums[k] + dp[k-1]
print(max(dp))
