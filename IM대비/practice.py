import sys
sys.stdin=open('input.txt','r')
def check(arr):
    global ans
    cnt=1
    for i in range(1,N):
        if arr[i-1] <= arr[i]:
            cnt+=1
        else:
            cnt=1

        if cnt>ans:
            ans=cnt


if __name__=='__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    ans=1
    check(arr)
    check(arr[::-1])
    print(ans)

