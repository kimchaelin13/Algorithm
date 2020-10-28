import sys
sys.stdin=open('input.txt','r')

'''

def make_permutaion(L):
    if L==m:
        for i in range(m):
            print(ans[i],end=" ")
        print()

    else:
        for i in range(1,n+1):
            if check[i]==0:
                check[i]=1
                ans[L]=i
                make_permutaion(L+1)
                check[i]=0



if __name__ == '__main__':
    n,m=map(int,input().split())
    ans=[0]*m
    check=[0]*(n+1)
    make_permutaion(0)
'''

'''
부분집합의 합 
-1 3 -9 6 7 -6 1 5 4 -2

합해서 0이 되는 부분집합을 모두 출력하시오

#1.0,0으로 출발해서
    선택했다가 선택안했다가 반복 => L이 끝까지 가면
    그때 합을 보고 0인지 아닌지, 0이면 출력
'''

def dfs(L,total):
    #global cnt

    if L==len(N):
        if total==0:
            for i in range(len(N)):
                if res[i]==1:
                    print(N[i],end=" ")
            print()

    else:
        res[L]=1
        dfs(L+1,total+N[L])
        res[L]=0
        dfs(L+1,total)


if __name__ == '__main__':
    N=list(map(int,input().split()))
    res=[0]*len(N)
    cnt=0
    dfs(0,0)
    #print(cnt)

