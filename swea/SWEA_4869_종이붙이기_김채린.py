import sys
sys.stdin = open("input1.txt", "r")

'''
dp[10]=1
'''
for tc in range(1,int(input())+1):
    N=int(input())
    dp=[]
    dp.append(1)
    dp.append(3)
    for i in range(2,N//10):
        dp.append(dp[i-1]+(dp[i-2]*2))
    print('#{} {}'.format(tc,dp.pop(-1)))

