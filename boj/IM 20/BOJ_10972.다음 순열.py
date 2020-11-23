import sys
sys.stdin=open('input.txt','r')



'''
#1 a[k] < a[k+1]인 가장 큰 인덱스 k를 찾는다.
만약 이를 찾을 수 없다면, 수열이 모두 역순으로 정렬된 것으로 사전식 순열의 맨마지막항이 됨

#2 k를 찾았다면 k이후의 인덱스에서 a[k]보다 크고, 또 가장 먼 인덱스 l를 찾는다
#3 k와 l 위치의 값을 swap
#4 그런다음 k보다 큰 인덱스 값들을 역순으로 배치한다.

1 2 3 4
'''

N=int(input())
nums=list(map(int,input().split()))

for i in range(1,N):
    if nums[i-1] < nums[i]:
        k = i-1

for j in range(k,N):
    if nums[j]>nums[k]:
        l = j

nums[k],nums[l]=nums[l],nums[k]

print(nums)

