import sys
sys.stdin=open('input.txt','r')
'''
#1.전체 K*K 배열 합 구하고
#2.테두리를 제외한 안쪽 부분 합 구해서
#3. #1-#2=> 첫번째 ans
#4. 가장 큰 걸로 갱신해준다
'''
for tc in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]

    #1.
    for i in range(N-K+1):
        for j in range(M-K+1):
            total=0
            for k in range(K):
                total+=sum(arr[i+k][j:j+K])

                #2.
                if k!=0 and k!=(K-1):
                    minus=sum(arr[i+k][])
