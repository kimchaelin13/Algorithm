

def DFS(L,sum):
    if L==n:
        if sum>N:
            return

    else:
        DFS(L+1,sum+arr[L])
        DFS(L,sum)

if __name__="__main__":
    W,N=map(int(input().split()))
    #arr을 받아서 무게 리스트를 작성해야하는데?

    DFS(0,0)