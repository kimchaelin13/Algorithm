import sys
sys.stdin=open('input.txt','r')

'''
9
1 2 2 4 4 5 7 7 2

0번부터 보다가 만약에 작은게 나오면? 그전까지의 길이를 저장하고,
작은것부터 다시 봄. 최종까지 갔을때 가장 긴 길이? 출력
'''
#
# def increase(nums):
#     start = 0
#     move = 0
#     end = 1
#     longest = 0
#     while True:
#         # 종료 조건
#         if (move == N-1) or (end == N - 1) or (start==N-1):
#             break
#         if nums[move] <= nums[end]:
#             end += 1
#             move += 1
#         else:
#             move = end
#             start = end
#             end = move + 1
#
#         if (end-start)+1>longest:
#             longest=(end-start)+1
#
#     return longest
#
#
# N=int(input())
# nums=list(map(int,input().split()))
# ans=0
# if increase(nums) > increase(nums[::-1]):
#     ans=increase(nums)
# else:
#     ans=increase(nums[::-1])
# print(ans)
#
#
#


def increase(nums):
    cnt = 1
    MAX = 1
    for i in range(1,N):
        if nums[i-1] <= nums[i]:
            cnt+=1
        else:
            if cnt>MAX:
                MAX=cnt
            cnt=1
        if cnt>MAX:
            MAX=cnt
    return MAX
N=int(input())
nums=list(map(int,input().split()))
ans=0
if increase(nums) >= increase(nums[::-1]):
    ans=increase(nums)
else:
    ans=increase(nums[::-1])
print(ans)

# def check(arr):
#     global ans
#     cnt=1
#     for i in range(1,N):
#         if arr[i-1] <= arr[i]:
#             cnt+=1
#         else:
#             cnt=1
#
#         if cnt>ans:
#             ans=cnt
#
#
# if __name__=='__main__':
#     N = int(input())
#     arr = list(map(int, input().split()))
#     ans=1
#     check(arr)
#     check(arr[::-1])
#     print(ans)
