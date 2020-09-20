import sys
sys.stdin = open("input.txt", "r")

def DFS(L,sum):
    global res
    if L>res: #레벨은 깊게 가는데, 답으로 갖고 있는 res보다 크다면 갈 필요가 없음
        return
    if sum>total:
        return

    if sum==total:
        if L<res:
            res=L
            print(res)


    else:
        for i in range(n):
            DFS(L+1,sum+coins[i])


if __name__=="__main__":
    n=int(input())
    coins=list(map(int,input().split()))
    total=int(input())
    res=987654321
    coins.sort(reverse=True)
    DFS(0,0)



