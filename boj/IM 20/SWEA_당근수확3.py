import sys
sys.stdin=open('input.txt','r')
'''
3
4 4
5 7 8 4
7 1 2 6
3 3 3 8
6 1 3 2

3번 사람이 마지막행만 한다고 고정
1번 그 행을 빼고, 
'''
'''
3
4 4
5 7 8 4
7 1 2 6
3 3 3 8
6 1 3 2
5 5
5 2 9 8 9
5 9 2 0 8
6 10 8 6 7
10 9 10 9 7
6 6 2 3 5
10 10
8 1 10 3 4 8 2 9 1 0
7 5 0 5 8 9 2 5 1 5
10 9 0 8 1 6 10 4 2 0
6 4 5 1 5 4 9 3 6 4
6 8 7 1 0 10 8 1 1 10
2 0 8 4 1 2 4 6 7 7
1 10 6 9 2 5 8 8 7 8
3 6 2 10 9 7 7 3 7 8
2 5 10 0 4 2 10 0 1 9
2 7 8 2 0 4 0 2 10 3
'''

T = int(input())
# T = 1
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # for row in arr:
    #     print(*row)
    minV = 9999999
    for i in range(1, N):   #3번영역과 1+2번 영역의 경계
        sum3 = 0
        for k in range(i,N):
            for m in range(0,M):
                sum3 += arr[k][m]
        # print("sum3 : ", sum3)
        for j in range(1,M):    #1번과 2번 영역의 경계
            sum1 = 0
            tMin = tMax = sum3
            for k in range(0,i):
                for m in range(0,j):
                    sum1 += arr[k][m]
            tMax = max(tMax,sum1)
            tMin = min(tMin,sum1)
            # print("sum1 : ", sum1)
            sum2 = 0
            for k in range(0,i):
                for m in range(j,M):
                    sum2 +=arr[k][m]
            tMax = max(tMax,sum2)
            tMin = min(tMin,sum2)
            minV = min(minV, abs(tMax-tMin))
            #농사 젤 잘한애 - 농사 젤 못한애의 격차가 작도록 당근 주자
            # print("sum2 : ", sum2)

    print("#{} {}".format(tc, minV))



# def check():
#     t=0
#     global MIN
#     w_1,w_2=0,0
#     while t<=M-1:
#         for i in range(0, k + 1):
#             w_1 += arr[i][t]
#         w_2 = total - w_1 - w_3
#         if max(w_1, w_2, w_3) - min(w_1, w_2, w_3) < MIN:
#             MIN = max(w_1, w_2, w_3) - min(w_1, w_2, w_3)
#         t += 1
#     return MIN
#
# for tc in range(1,int(input())+1):
#     N,M=map(int,input().split())
#     arr=[list(map(int,input().split())) for _ in range(N)]
#     total=0
#     for x in arr:
#         total += sum(x)
#     w_3=0
#     MIN=987654321
#     for k in range(N-1)[::-1]:
#         w_3 += sum(arr[k+1][:])
#         check()
#     print('#{} {}'.format(tc,MIN))