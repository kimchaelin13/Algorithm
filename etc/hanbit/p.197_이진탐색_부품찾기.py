import sys
sys.stdin = open('input.txt','r')

N=int(input())
stock=list(map(int,input().split()))
stock.sort()
M=int(input())
request=list(map(int,input().split()))


for i in request:
    target=i
    start=0
    end=N-1
    answer='no'
    while (start<=end):
        mid=(start+end)//2
        if stock[mid]==target:
            answer='yes'
            break
        elif stock[mid]>target:
            end=mid-1
        else:
            start=mid+1
    print(answer,end=' ')
