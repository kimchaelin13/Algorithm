import sys
sys.stdin=open('input.txt','r')

for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,input()))
    #print(nums)
    MAX=0
    result=0
    for i in range(N):
        cnt=0
        cnt=nums.count(nums[i])

        if cnt>MAX:
            MAX=cnt
            result=nums[i]

            if MAX==1:
                result=max(nums)
    print(result,MAX)
