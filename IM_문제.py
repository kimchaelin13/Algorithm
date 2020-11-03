'''
암호, 신호 0~9 숫자
0개 이상 숫자 제거 시 암호와 동일해진다면 해당 신호는 암호를 포함한 신호
암호 포함한 신호 라면 1 출력, 아니라면 0 출력
신호를 보는데 만약 암호와 같은 것이 나왔다면 암호를 0으로 바꾸고 만약 전부 0으로 바뀌지 않는다면 0출력
다 바뀌면 1 출력
'''
import sys

sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    # 신호의 길이N, 암호의 길이K
    N, K = map(int, input().split())
    # 신호
    signal = list(map(int, input().split()))
    # 암호
    code = list(map(int, input().split()))
    # print(signal)
    # print(code)
    idx = -1  # 찾은암호 idx보다 뒤부터!
    for k in range(K):
        for n in range(idx + 1, N):
            if code[k] == signal[n]:
                code[k] = 0
                idx = n
                break
                # print(code)
    # code가 0 이 아니라면, 신호에 암호가 포함되지 않음
    if sum(code):
        # print(code,'1')
        print('#{} 0'.format(tc))

    else:
        # print(sum(code))
        print('#{} 1'.format(tc))