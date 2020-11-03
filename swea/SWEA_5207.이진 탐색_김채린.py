import sys
sys.stdin=open('input.txt','r')
'''
오른쪽,오른쪽 보거나 왼,왼 보면 안됨 
'''
def find_m(arr,target,start,end):
    global cnt
    l,r=0,0
    while start<=end:
        mid=(start+end)//2
        if (arr[mid]==target):
            cnt+=1
            return cnt
        elif not l and arr[mid] > target:
            end=mid-1
            l=1
            r=0
        elif not r and arr[mid]<target:
            start=mid+1
            r=1
            l=0
        else:
            return

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    N_list=sorted(list(map(int,input().split())))
    M_list=list(map(int,input().split()))
    cnt=0
    for target in M_list:
        find_m(N_list,target,0,N-1)
    print('#{} {}'.format(tc,cnt))
