import sys
sys.stdin=open('input.txt','r')


# def is_increase(num):
#     st = str(num)
#     for s in range(len(st)):
#

# for tc in range(1,int(input())+1):
#     N=int(input())
#     nums=list(map(int,input().split()))
#
#     temp=0
#     for i in range(0,N-1):
#         for j in range(i+1,N):
#             temp=nums[i]*nums[j]
#             print(temp)
#             is_increase(temp)
def is_increase(num):
    str_num = str(num)

    for i in range(len(str_num)-1):
        if str_num[i]>str_num[i+1]:
            return False
    return True

for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,input().split()))

    temp=0
    MAX=-1
    for i in range(0,N-1):
        for j in range(i+1,N):
            temp=nums[i]*nums[j]
            if MAX<temp and is_increase(temp):
                MAX = temp
    print('#{} {}'.format(tc,MAX))

