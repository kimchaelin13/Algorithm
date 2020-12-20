import sys
sys.stdin=open('input.txt','r')

'''
4 6
19 15 10 17

min 6만큼 떡을 얻기 위해서는 절단기 h를 어떻게 해야할까?

'''

n,m=map(int,input().split())
arr=list(map(int,input().split()))

start=0
end=max(arr)

#d이진탐색 수행(반복)
result=0
while start<=end:
    total=0
    mid=(start+end)//2
    for x in arr:
        #잘랐을때의 양 계산
        if x>mid:
            total += x-mid
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total<m:
        end=mid-1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result=mid
        start=mid+1
print(result)