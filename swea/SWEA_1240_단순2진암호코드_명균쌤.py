import sys
sys.stdin=open('input.txt','r')

'''


'''


pattern = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4, "0110001": 5, "0101111": 6,
           "0111011": 7, "0110111": 8, "0001011": 9}


def check(n):
    zero_cnt = 0
    for i in range(len(n) - 1, -1, -1):
        if n[i] == "1":
            break
        zero_cnt += 1

    ed = len(n) - zero_cnt
    # 8자리의 암호코드를 집어 넣었다.
    tmp = n[ed - 56:ed]

    change_code = []
    # 정해놓은 딕셔너리를 통해 변환된 숫자값을 넣는다.
    for i in range(0, len(tmp), 7):
        change_code.append(pattern[tmp[i:i + 7]])

    odd = 0
    even = 0

    for i in range(len(change_code)):
        if i % 2:
            even += change_code[i]
        else:
            odd += change_code[i]

    if (odd * 3 + even) % 10:
        return 0
    else:
        return sum(change_code)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 행과 열

    code = [input() for _ in range(N)]

    for i in range(N):
        # 1이라는 값이 들어있다면 그 행은 암호코드
        if "1" in code[i]:
            ans = check(code[i])
            break

    print("#{} {}".format(tc, ans))