import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N=int(input())
    farm=[list(map(int,input())) for _ in range(N)]
    total=[]
    for i in range(N):
        middle=N//2
        if i < middle:
            total.extend(farm[i][middle-i:middle+i+1])

        else:
            total.extend(farm[i][i-middle:middle-i])
    print(sum(total))



T = int(input())
# print(T)
# for tc in range(1,T+1):
#     N = int(input())
#     # print(N)
#     arr = [list(map(int,input())) for _ in range(N)]
#     # print(f'#{tc} {arr}')
#     SUM = []
#     for i in range(N):
#         #행 idx 반을 넘어가면 2만큼 슬라이싱이 줄어듦 [1:-1] [2:-2]..이런식으로 됨
#         if N//2 < i:
#             SUM.extend(arr[i][i-N//2:N//2-i])
#             # print(arr[i][i-N//2:N//2-i])
#             # print(SUM)
#         #행idx가 반이 될때까지 slicing이 중간에서 2씩 늘어남
#         else:
#             SUM.extend(arr[i][N//2 - i:N//2+i+1])
#             # print(arr[i][N//2 - i:N//2+i+1])
#             # print(SUM)
#
#
#
#     # print(SUM)
#     print('#{} {}'.format(tc,sum(SUM)))