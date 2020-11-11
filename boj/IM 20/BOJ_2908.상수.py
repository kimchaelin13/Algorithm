import sys
sys.stdin=open('input.txt','r')


# def reverse(num):
#     res=''
#     for i in range(3):
#         res += str(num%10)
#         num = num//10
#     return res
#
# nums=list(map(int,input().split()))
# result=[]
# for i in range(2):
#     result.append(int(reverse(nums[i])))
# print(max(result))

a,b=input().split()

def reading(num):
    num = num[::-1]
    return int(num)
print(max(reading(a),reading(b)))
