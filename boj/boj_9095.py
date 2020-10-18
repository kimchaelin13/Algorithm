import sys
sys.stdin=open('input.txt','r')

dp=[1,2,4]


for i in range(3,10):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for _ in range(int(input())):
    n=int(input())
    print(dp[n-1])
