import sys
sys.stdin=open('input.txt','r')
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid=len(unsorted_list)//2

    left=unsorted_list[:mid]
    right=unsorted_list[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1,right1)

def merge(left,right):
    global cnt
    left_N, right_N = len(left), len(right)
    result=[0]*(left_N+right_N)
    left_i,right_i=0,0
    i=0
    if left[-1] > right[-1]:
        cnt += 1
    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i +=1
            left_i +=1
        else:
            result[i] += right[right_i]
            i +=1
            right_i +=1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i +=1
            left_i +=1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i+=1
            right_i+=1

    return result


for tc in range(1,int(input())+1):
    N=int(input())
    arr=list(map(int,input().split()))
    cnt=0
    result=merge_sort(arr)
    print('#{} {} {}'.format(tc,result[N//2],cnt))