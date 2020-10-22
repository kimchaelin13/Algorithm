import sys
sys.stdin=open('input.txt','r')


def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)


for _ in range(int(input())):
    nums=list(map(int,input().split()))[1:]
    ans=[]
    for j in range(len(nums)):
        for k in range(j+1,len(nums)):
            answer=gcd(nums[j],nums[k])
            ans.append(answer)
    print(sum(ans))

