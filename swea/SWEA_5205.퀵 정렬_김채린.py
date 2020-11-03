import sys
sys.stdin=open('input.txt','r')

def quick_sort(arr,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end

    while left<=right:
        while left<=end and arr[left]<=arr[pivot]:
            left+=1
        while right>start and arr[right]>=arr[pivot]:
            right-=1
        if left>right:
            arr[right],arr[pivot]=arr[pivot],arr[right]
        else:
            arr[left],arr[right]=arr[right],arr[left]
        if left>right: quick_sort(arr,start,right-1)
        if right<left: quick_sort(arr,right+1,end)



for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,input().split()))
    quick_sort(nums,0,N-1)
    print('#{} {}'.format(tc,nums[N//2]))


# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot=arr[0]
#     tail=arr[1:]
#
#     left_side=[x for x in tail if x <= pivot]
#     right_side=[x for x in tail if x>pivot]
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# for tc in range(1,int(input())+1):
#     N=int(input())
#     arr=list(map(int,input().split()))
#     result=quick_sort(arr)
#     print('#{} {}'.format(tc,result[N//2]))