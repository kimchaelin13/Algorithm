#상하좌우로 풀면 안됨
#우하좌상으로 구현해야 달팽이 출력 가능

import sys
sys.stdin = open("input.txt", "r")
# 우 하 좌 상

#
dr= [0,1,0,-1]
dc= [1,0,-1,0]

T = int(input())

for t in range(1,T+1):
    N=int(input())

    arr=[[0]*N for _ in range(N)]

    d=0 #방향 0: 우, 1:하, 2:좌, 3:상, 각각의 번호는 인덱스를 의미한다.
    r=0
    c=0
    num=1

    while num <= N*N:
        arr[r][c] =num #현재칸에 값을 저장
        num += 1 #다음 숫자 준비

        #다음칸을 결정
        nr = r+dr[d]
        nc = c+dc[d]
        #범위를 벗어나기 전에 방향을 꺾어줘야 함

        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
            #현재좌표를 nr,nc로 갱신
            r,c = nr,nc
        else:
            #상까지 갔을때 우로 바꿔야 하는데 상은 3이고, 우는 0이다.그래서
            #모듈러 연산으로!! 좌표를 바꿔주고 한칸씩 답을 갱신
            #1,2로 바꿔줌줌
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=" ")
        print()


# #2
#
# T=int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     nums = [[0]*N for _ in range(N)]
#
#     K=N #이동거리
#     d=1 #방향
#     row=0 #행
#     col=-1 #열, 초기에는 수평이동이므로 -1로 초기화
#     num =1 #넣을 값
#
#     while True:
#         #수평이동
#         for c in range(K):
#             col+=d
#             nums[row][col] =num
#             num+=1
#         #수평이동 끝 이제 수직 이동
#         #포인트@ 수평끝나고 수직할때 k=-1해주고
#         K -=1
#         if K ==0:
#             break
#         #수직이동
#         for r in range(K):
#             row+=d
#             nums[row][col] = num
#             num += 1
#         #수직이동이 끝 수평이동
#         #방향이 바뀔때 d를 -곱해주고, 뭐그런식, 뭔가 어제내가푼거랑 비슷한느낌,,,
#         d *= -1
#     print('#{}'.format(tc))
#     for i in range(N):
#         for j in range(N):
#             print(nums[i][j],end=" ")
#         print()

