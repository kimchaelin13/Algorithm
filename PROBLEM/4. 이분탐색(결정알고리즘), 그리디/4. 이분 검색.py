import sys
sys.stdin = open('input.txt','r')

n,m = map(int, input().split())
a=list(map(int,input().split()))
#이분검색을 하기위해서는 기본적으로 오름차순이든 내림차순이든 정렬을 해야한다.
a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1





# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# tmp=sorted(a)
# res=0
#
# ans=tmp.index(m)
# print(ans+1)