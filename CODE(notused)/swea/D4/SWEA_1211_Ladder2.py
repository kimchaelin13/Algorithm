import sys
sys.stdin = open("input2.txt", "r")

'''
Ladder1 문제랑 차이점 : 도착지점들은 2로 표현되지 않고 모든 갈 수 있는 길은 1이다. 가장 먼저 사다리가 도착하는 경우의 시작 x 좌표가 어딘지 출력하세요
첫번째 인덱스부터 내려오기, 근데 일단 1이 어디에 있는지 찾아야하고, 그 x에서만 내려올거임
내려오는거니까, 업은 안해도되고 only focus on down, left, right! 여기서 right/left가 무한반복에 빠지지 않도록
(0 1 1 이면 0에서 1로 왔는데 다시 왼쪽으로 안가게 move를 설정해줌 left에서 왔으면 left로만 right는 right로만 갈수있게)
가장 짧은 걸 선택해야되니까, 일단 처음에 숫자를 크게 잡아놓고, 각각 내려올떄마다 카운트해주고, 
가장 min일때 그걸로 갱신하고, 그떄의x를 뽑음
'''

# for tc in range(1,11):
#     n=int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]
#     start_list = [i for i in range(100) if ladder[0][i] == 1]
#     mini=10000
#     start_x=0
#
#     for start in start_list:
#         move=0
#         cnt=0
#         dy=0 #
#         dx=start
#         while dy<99 :
#             #left
#             if (move==3 or move==1) and dx>0 and ladder[dy][dx-1]==1:
#                 move=1
#                 dx-=1
#             #right
#             elif (move==3 or move==2) and dx<99 and ladder[dy][dx+1]==1:
#                 move=2
#                 dx+=1
#             #down
#             else:
#                 move=3
#                 dy +=1
#
#             cnt+=1
#
#         if mini > cnt:
#             mini = cnt
#             start_x = start
#
#     print('#{} {}'.format(tc,start_x))

for tc in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start_list = [i for i in range(100) if ladder[0][i] == 1]
    min_cnt = 10000
    start_dx = 0

    for start in start_list:
        dy = 0
        dx = start ##
        move = 0
        cnt = 0
        while dy < 99:
            # left
            if (move == 1 or move == 3) and dx > 0 and ladder[dy][dx - 1] == 1:
                move = 1
                dx -= 1
            elif (move == 2 or move == 3) and dx < 99 and ladder[dy][dx + 1] == 1:
                move = 2
                dx += 1
            else:
                move = 3
                dy += 1
            cnt += 1

        if min_cnt > cnt:
            min_cnt = cnt
            start_dx = start
    print('#{} {}'.format(tc, start_dx))





