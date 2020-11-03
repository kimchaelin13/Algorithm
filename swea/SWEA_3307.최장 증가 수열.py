import sys
sys.stdin=open('input.txt','r')


'''
2
5
1 3 2 5 4
6
4 2 3 1 5 6

'''
'''
LIS를 다 채워서 리턴하는 함수다

넘버를 보면서 자기보다 작은 넘버가 갖고있는 VALUE값중에 가장 큰거에 하나 더한다.
'''
for tc in range(1,int(input())+1):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    DP = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i, 1):
            if a[i] > a[i - j]:
                DP[i] = max(DP[i - j], DP[i])
        DP[i] += 1
    print('#{} {}'.format(tc,max(DP)))

# def make_LIS(nums,LIS):
#     s=1
#     for i in range(s,N):
#         MAX=1
#         for j in range(0,s):
#             if nums[i] > nums[j]:
#                 if LIS[j]>=MAX:
#                     MAX=LIS[j]
#         LIS[i]=MAX+1
#         s += 1
#     print(LIS)
#     return LIS
#
#
# for tc in range(1,int(input())+1):
#     N=int(input())
#     nums=list(map(int,input().split()))
#     LIS=[1]*N
#     # LIS={}
#     # for i in nums:
#     #     LIS[i]=1
#     # print(LIS)
#     result=make_LIS(nums,LIS)
#     print('#{} {}'.format(tc,max(result)))