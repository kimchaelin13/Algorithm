import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N:화덕의 크기/M:피자수
    cheeze = [0] + list(map(int, input().split()))  # 1

    oven = [[i, cheeze[i]] for i in range(1, N + 1)]  # 2, 피자번호
    remain = [[i, cheeze[i]] for i in range(1, N + 1)]
    pos = N + 1  # 추가될 피자번호

    while len(oven) > 1:  # 한개가 되면 팝할거임
        num, cheese = oven.pop(0)
        cheeze = cheeze // 2
        if cheeze:  # 원래위치에 집어넣는게아니라 뒤쪽에 집어넣어도 같은 결과
            oven.append([num, cheeze])
        else:
            if remain:
                oven.append(remain.pop(0))

    print('#{} {}'.format(tc,oven[0]))