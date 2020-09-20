
'''
3
1 2 5
15
'''

def DFS(L,sum):
    global res
    if L>res:
        return  #cutedge2
    if sum>m: #sum이 15를 넘어가면 컷해주고,cut edge1
        return
    if sum==m: #sum=15면 답을 찾는거다
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])


    else:
        for i in range(1,n+1):
            DFS(L+1,sum+coins[L])



if __name__ =="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    res=2132211 #답을 최소로 해야하니까
    a.sort(reverse=True) #가장 큰 동전부터 적용하려고!
    DFS(0,0)