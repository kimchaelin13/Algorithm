
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    if N > M:
        result ='>'
    elif N < M:
        result = '<'
    else:
        result = '='
    print(f'#{test_case} {result}')
