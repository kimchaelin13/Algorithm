import sys
sys.stdin=open('input.txt','r')
def min_production_cost(L,total):
    global MIN
    if total > MIN:
        return
    if L==N:
        if MIN > total:
            MIN=total
    else:
        for i in range(N):
            if check[i]==0:
                check[i]=1
                min_production_cost(L+1,total+arr[i][L])
                check[i]=0

for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    check=[0]*N
    MIN=987654132
    min_production_cost(0,0)
    print('#{} {}'.format(tc,MIN))

