import sys
sys.stdin = open("input2.txt", "r")

# for tc in range(1,int(input())+1):
#     N,M=map(int,input().split())
#     arr=[list(input()) for _ in range(N)]
#     result = M - arr[0].count('W')
#     #print(result)
#
#     #1행부터 파랑으로 할지 흰으로 할지 결정, 중간에,
#     # 근데 여기서 파랑색이 무조건 있어야됨, 파란색으로 못만들면? 파란색으로 만들기 못함??
#     for i in range(1,N-1):
#             if arr[i].count('W') >= arr[i].count('B'):
#                 result+=M-arr[i].count('W')
#             else:
#                 result+= M-arr[i].count('B')
#
#     result+= M-arr[N-1].count('R')
#     print(result)
#하영이가 힌트줬댷
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 행렬의 크기 3~50
    arr = [list(input()) for _ in range(N)]
    MIN = 10000000
    # 1 for문으로 경우 전부 계산
    cnt_w = 0
    for w in range(0, N-2):  # 화이트
        for k in range(0, M):
            if arr[w][k] != 'W':
                cnt_w += 1

        cnt_b = 0
        for b in range(w+1,N-1):  # 블루
            for k in range(0, M):
                if arr[b][k] != 'B':
                    cnt_b += 1

            cnt_r = 0
            for r in range(b + 1, N):  # 레드
                for k in range(0, M):
                    if arr[r][k] != 'R':
                        cnt_r += 1

            if MIN > cnt_w+ cnt_b+ cnt_r:
                MIN = cnt_w+ cnt_b+ cnt_r
    print('#{} {}'.format(tc,MIN))




for tc in range(1,T+1):
    N,M=map(int,input().split())
    #각 행에 색 카운트
    w=[0]*N
    b = [0] * N
    r = [0] * N


    #w,b,r이 몇개가 칠해져 있는지!!
    for i in range(N):
        color=input()
        w[i]=color.count('W')
        b[i] = color.count('W')
        r[i] = M-w[i]-b[i]

    #누적합 구하기(나중에 한번에 계산하기 위해서)
    for i in range(1,N):
        w[i] += w[i-1]
        b[i] += b[i - 1]
        r[i] += r[i - 1]

    ans=N*M
    for i in range(N-2):
        for j in range(i+1,N-1):
            #흰색 칠하기
            cnt=M*(i+1)-w[i]
            #파란색 칠하기
            cnt=M*(j-1)-(b[j]-b[i])
            #빨간색 칠하기
            cnt += M*(N-1-j)-(r[N-1]-r[j])
            ans=min(ans,cnt)
    print('#{} {}'.format(tc,ans))

