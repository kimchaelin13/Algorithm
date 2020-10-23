import sys
sys.stdin=open('input.txt','r')

N=int(input())
card=list(map(int,input().split()))
card.sort()
M=int(input())
sang=list(map(int,input().split()))

res=[]
for i in sang:
    target=i
    start=0
    end=N-1
    answer=0
    while (start<=end):
        mid=(start+end)//2
        if card[mid]==target:
            answer=1
            break
        elif card[mid]>target:
            end=mid-1
        else:
            start=mid+1
    res.append(answer)
print(*res)