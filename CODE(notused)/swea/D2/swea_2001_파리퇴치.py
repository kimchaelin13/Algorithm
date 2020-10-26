import sys
sys.stdin = open("input1.txt", "r")


# def flapper(r,c):
#     sum = 0
#     for i in range(r,r+M):
#         for j in range(c,c+M):
#             sum += flies[i][j]
#     return sum
#
#
#
# for tc in range(1,int(input())+1):
#     N,M=map(int,input().split())
#     flies=[list(map(int,input().split())) for _ in range(N)]
#
#     ans = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             tmp=flapper(i,j)
#             if ans<tmp:
#                 ans=tmp
#
#     print("#{} {}".format(tc,ans))



# def flapper(ㅛ,ㅏ):
#     sum=0
#     for i in range(r,r+M):
#         for j in range(c,c+M):
#             sum+=flies[i][j]
#     return sum


# for tc in range(1,int(input())+1):
#     N,M=map(int,input().split())
#     flies=[list(map(int,input().split())) for _ in range(N)]
#
#     ans=0
#     for r in range(N-M+1):
#         for c in range(N-M+1):
#             tmp=flapper(r,c)
#             if ans<tmp:
#                 ans=tmp
#     print('#{} {}'.format(tc,ans))

T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = []
    for i in range(N):
        flies.append(list(map(int, input().split())))

    killed = []
    for v in range(N-M+1):
        for h in range(N-M+1):
            s = 0
            for m in range(M):
                s += sum(flies[v+m][h:h+M]) #1
            killed.append(s)

    print(f'#{tc} {max(killed)}')