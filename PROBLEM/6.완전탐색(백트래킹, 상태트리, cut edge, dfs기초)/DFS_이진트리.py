import sys

sys.stdin = open('input.txt', 'r')


def DFS(v):
    # 종료조건
    if v > 7:
        return

    else:
        # 왼쪽자식 호출
        DFS(v * 2)
        # 함수 본연의 일! 출력
        print(v, end=" ")
        # 오른쪽자식 호출
        DFS(v * 2 + 1)


if __name__ == "__main__":
    DFS(1)