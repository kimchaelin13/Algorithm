import sys
sys.stdin = open("input.txt", "r")

def DFS(L,sum):

    if L==n:
        if sum==total-sum:
            print('YES')
            sys.exit()
    else:
        DFS(L+1,sum+nums[L])
        DFS(L+1,sum)



if __name__=="__main__":
    n=int(input())
    nums=list(map(int,input().split()))
    total=sum(nums)
    DFS(0,0)
    print('NO')

