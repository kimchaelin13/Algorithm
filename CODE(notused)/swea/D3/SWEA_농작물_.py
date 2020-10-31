import sys
sys.stdin = open("input3.txt", "r")
from collections import deque

for tc in range(1,int(input())+1):
    n = int(input())
    farm=[list(map(int,input())) for _ in range(n)]
    #print(farm)
    check = [[0] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    sum = 0
    Q = deque()

    check[n // 2][n // 2] = 1
    Q.append((n // 2, n // 2))
    sum += farm[n // 2][n // 2]
    L = 0

    while True:
        if L == n // 2:
            break

        else:
            size = len(Q)
            for i in range(size):
                tmp = Q.popleft()
                for j in range(4):
                    x = tmp[0] + dx[j]
                    y = tmp[1] + dy[j]
                    if check[x][y] == 0:
                        sum += farm[x][y]
                        check[x][y] = 1
                        Q.append((x, y))
            L += 1
    print('#{} {}'.format(tc,sum))