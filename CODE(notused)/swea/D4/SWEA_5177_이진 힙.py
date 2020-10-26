import sys
import heapq as hq
sys.stdin = open("input.txt","r")

for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,input().split()))
    
    for n in nums:
        hq.heappush(nums,n)
    print('#{} {}'.format(tc,hq.heappop(nums)))
    