import sys
sys.stdin=open('input.txt','r')

'''
#1. sum을 갖고 다니면서 출발
#2. 레벨 끝까지 왔을때 sum(number)==total:
                        return True
'''


def dfs(L,total):
    global ans
    if total>sum(nums)//2:
        return
    if L==N:
        if sum(nums)-total==total:
            ans='YES'

    else:
        dfs(L+1,total+nums[L])
        dfs(L+1,total)

if __name__ == '__main__':
    N=int(input())
    nums=list(map(int,input().split()))
    ans='NO'
    dfs(0,0)
    print(ans)