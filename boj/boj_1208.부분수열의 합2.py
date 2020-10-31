import sys
sys.stdin=open('input.txt','r')


'''

'''
n,m=map(int,input().split())
a = list(map(int,input().split()))
lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot!=m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)
# N,S=map(int,input().split())
# nums=list(map(int,input().split()))
# lt=0
# rt=1
# cnt=0
# total=nums[0]
#
# while True:
#     if total<S:
#         if rt<N:
#             total+=nums[rt]
#             rt+=1
#         else:
#             break
#     elif total == S:
#         cnt+=1
#         total-=nums[lt]
#         lt+=1
#     else:
#         total-=nums[lt]
#         lt+=1
#
# print(cnt)

# def dfs(L,total):
#     cnt=0
#     if L==N:
#         if total==S:
#             cnt+=1
#     else:
#         dfs(L+1,total+nums[L])
#         dfs(L+1,total)
#
#     return cnt
#
# if __name__ == '__main__':
#     N,S=map(int,input().split())
#     nums=list(map(int,input().split()))
#     print(dfs(0,0))