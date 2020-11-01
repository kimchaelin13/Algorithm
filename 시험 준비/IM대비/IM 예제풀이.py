import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    N,P=map(int,input().split())
    ans=list(map(int,input().split()))
    res=[]

    for _ in range(N):
        tes=list(map(int,input().split()))

        tmp=0
        score=0
        for i in range(P):
            if ans[i]==tes[i]:
                tmp+=1
            else:
                tmp=0

            score+=tmp
        res.append(score)

    print('#{} {}'.format(tc,max(res)-min(res)))