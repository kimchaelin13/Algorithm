import sys
sys.stdin=open('input.txt','r')

dp=[1,2]
for i in range(2,1000):
    dp.append(dp[i-2]+dp[i-1])
#print(dp)

n=int(input()) #n은9, dp의 인덱스상으로는 dp[8]번째
print(dp[n-1]%10007)