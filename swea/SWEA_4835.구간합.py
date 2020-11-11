import sys
sys.stdin=open('input.txt','r')

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    nums=list(map(int,input().split()))
    res=[]
    temp=0
    for i in range(N-M+1):
        temp = sum(nums[i:i+M])
        res.append(temp)
    print('#{} {}'.format(tc,max(res)-min(res)))