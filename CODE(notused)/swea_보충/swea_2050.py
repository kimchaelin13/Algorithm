import sys
sys.stdin = open("input.txt", "r")

alpha=input()
nums = []
result=''
num=1
for i in range(1,len(alpha)+1):
    nums.append(i)
    num+=1
nums = ''.join(str(nums))
print(nums)





