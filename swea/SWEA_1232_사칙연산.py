import sys
sys.stdin = open("input2.txt", "r")


def make(start, end):
    for i in range(end, start - 1, -1):
        if p[i] == '/':
            p[i] = p[c1[i]] / p[c2[i]]
        elif p[i] == '+':
            p[i] = p[c1[i]] + p[c2[i]]
        elif p[i] == '-':
            p[i] = p[c1[i]] - p[c2[i]]
        elif p[i] == '*':
            p[i] = p[c1[i]] * p[c2[i]]


for tc in range(1, 11):
    N=int(input())
    p = [0] * (N + 1)
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    for i in range(N):
        line = input().split()
        if len(line) == 4:
            p[int(line[0])] = line[1]
            c1[int(line[0])] = int(line[2])
            c2[int(line[0])] = int(line[3])
        else:
            p[int(line[0])] = int(line[1])
    make(1, N)
    print("#{} {}".format(tc, int(p[1])))