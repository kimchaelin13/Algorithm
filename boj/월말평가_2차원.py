import sys
sys.stdin=open('input.txt','r')
'''
#1.전체 K*K 배열 합 구하고
#2.테두리를 제외한 안쪽 부분 합 구해서
#3. #1-#2=> 첫번째 ans
#4. 가장 큰 걸로 갱신해준다


11 75 97 9 36
14 33 72 12 57
44 77 38 98 67
38 30 69 16 48
45 29 35 64 56
23 75 48 87 45
'''
for tc in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    res=[]
    #1.
    for i in range(N-K+1):
        for j in range(M-K+1):
            total=minus=0
            for k in range(K):
                total+=sum(arr[i+k][j:j+K])

                #2.
                if k!=0 and k!=(K-1):
                    minus += sum(arr[i+k][j+1:j+K-1])
            res.append(total-minus)

    print('#{} {}'.format(tc,max(res)-min(res)))