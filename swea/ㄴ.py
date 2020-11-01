for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans=0

    H = [0] * (N + 1)
    hsize = 0  # 스택의 탑

    for val in arr:
        hsize += 1
        H[size] = val

        c = hsize;
        p = hsize // 2
        while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p;
            p = c // 2
    v = N // 2
    while v:
        ans += H[v]
        v = v // 2
    print('#{} {}'.format(tc, ans))