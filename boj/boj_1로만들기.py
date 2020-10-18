import sys
sys.stdin=open('input.txt','r')

dp=[0,0,1]
n=int(input())
for i in range(3,n+1):
    if (i%2==0 and i%3==0):
        dp.append(min(dp[i-1]+1,dp[i//2]+1,dp[i//3]+1))
    elif i%2==0:
        dp.append(min(dp[i-1]+1,dp[i//2]+1))
    elif i%3==0:
        dp.append(min(dp[i-1]+1,dp[i//3]+1))
    else:
        dp.append(dp[i-1]+1)
print(dp[n])