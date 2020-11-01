import sys
sys.stdin=open('input.txt','r')

'''
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

#1.배열을 받고
#2.(N-K+1)만큼만 돌아야하니까 FOR문 두개로 범위를 정해놓는다
#3.그리고 
'''
def max_flies(arr,N,K):
    res=0
    for i in range(N-K+1):
        for j in range(N-K+1):
            total=0
            for k in range(K):
                total+=sum(arr[i+k][j:j+K])
            # for rk in range(i,i+K):
            #     for ck in range(j,j+K):
            #         total+=arr[rk][ck]
            if total>res:
                res=total
    return res

for tc in range(1,int(input())+1):
    N,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_flies(arr,N,K)
    print('#{} {}'.format(tc,max_flies(arr,N,K)))