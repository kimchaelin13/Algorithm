import sys
sys.stdin=open('input.txt','r')

'''
1.1 0.7 1.3 0.9 1.4 0.8 0.7 1.4

1.1을 반드시 포함하면서, 만들수 있는 연속최대곱 길이는?

투포인터

s=0
e=1

8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4


'''

N=int(sys.stdin.readline())
nums=[]
for _ in range(N):
    nums.append(float(sys.stdin.readline()))
s=0
e=1
MAX=nums[s]
temp=nums[s]
while True:
    if s==N or e==N:
        break
    if temp*nums[e]<=MAX:
        s=e
        e+=1
        temp=nums[s]
    else:
        MAX=temp*nums[e]
        e+=1
        temp=MAX
print('%0.3f'% MAX)