'''
NxN배열에 숫자가 들어있음
한줄에 하나씩 N개의 숫자를 골라 합이 최소가 되게하려함
한줄에 하나, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음.
'''
import sys
sys.stdin = open('input.txt', 'r')


def perm(i, sum):
    global MIN
    # sum이 MIN보다 크거나 같으면 종료
    if sum >= MIN:
        return
    # idx가 N과 같아지면
    if i == N:
        # 저장된 MIN과 sum을 비교해서 MIN보다 작으면 갱신함
        if MIN > sum:
            MIN = sum
        return

    for k in range(N):
        # 방문표시 했다면 지나가라
        if visited[k]:
            continue
        # 방문을 했다고 표시
        visited[k] = True
        # 다음 idx로 함수 호출, 그 값을 더해준것을 같이 보냄
        perm(i + 1, sum + board[i][k])
        # 다시 방문 표시 원상 복구
        visited[k] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    visited = [False for i in range(N)]
    MIN = 9999999
    perm(0, 0)
    print('#{} {}'.format(tc, MIN))