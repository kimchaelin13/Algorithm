import sys
sys.stdin=open('input.txt','r')

'''
10 20 30 40


'''

nums=list(input().split())
#print(nums)
fir=''
sec=''

for i in range(1):
     fir=nums[i]+nums[i+1]
     sec=nums[i+2]+nums[i+3]


print(int(fir)+int(sec))
