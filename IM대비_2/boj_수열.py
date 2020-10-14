import sys
sys.stdin=open('input.txt','r')
'''
오름차순, 내림차순으로 cnt를 모두 각각 구해서 그중에 큰걸로 res해야지
-> 틀린 이유 : 이렇게 하면 연속이 안됨 계속 더해지는거임, 그래서 아니면 바로 1로 초기화해줘야함
'''
# n=int(input())
# nums=list(map(int,input().split()))
#
# #오름차순
# cnt1=0
# for i in range(n):
#     if i<n-1:
#         if nums[i]<=nums[i+1]:
#             cnt1+=1
#         else:
#             cnt1=1
#     if i==n-1:
#         if nums[i-2]<=nums[i-1]:
#             cnt1+=1
#         else:
#             cnt1=1
# # print(cnt1)
#
# #내림차순
# cnt2=0
# nums2=list(reversed(nums))
# for i in range(n):
#     if i<n-1:
#         if nums2[i]<=nums2[i+1]:
#             cnt2+=1
#         else:
#             cnt2=1
#     if i==n-1:
#         if nums2[i-2]<=nums2[i-1]:
#             cnt2+=1
# # print(cnt2)
#
# if cnt1>=cnt2:
#     print(cnt1)
# else:
#     print(cnt2)


def check(arr):
    global ans
    cnt=1

    for i in range(1,n):
        if arr[i-1] <= arr[i]: #이렇게하면 인덱스에러애서 자유로운듯
                            #왜냐면 i를 +하지 않으니까!
                            #i는 1,2,3,4,5,6,7,8
                            #이거를 그냥 외워두자, 연속비교수열
            cnt+=1
        else:
            cnt=1
        if cnt>ans:
            ans=cnt


if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    ans=1
    check(arr)
    check(arr[::-1])
    print(ans)