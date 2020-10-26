arr = [1, 2, 3]
N = 3

sel = [0] * N


def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for i in range(N):
        if (check & (1 << i)) != 0:
            continue

        sel[idx] = arr[i]
        perm(idx + 1, check | (1 << i))


perm(0, 0)
