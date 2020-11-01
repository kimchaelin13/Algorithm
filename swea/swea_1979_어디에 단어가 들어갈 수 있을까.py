import sys
sys.stdin = open("input1.txt", "r")

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]

    result=0
    for i in range(N):
        sum = 0
        for j in range(N):
            if arr[i][j] == 1:
                sum+=1
                if sum==K:
                    result+=1
            else:
                sum=0

            if sum>K:
                result-=1
                sum=0

    for i in range(N):
        sum = 0
        for j in range(N):
            if arr[j][i]==1:
                sum+=1
                if sum==K:
                    result+=1
            else:
                sum=0

            if sum>K:
                result-=1
                sum=0
    print('#{} {}'.format(tc,result))



