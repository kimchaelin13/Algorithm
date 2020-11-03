import sys
sys.stdin=open('input.txt','r')


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ##호출한 밑 라인은 백하는 지점이다.체크를 풀어줘야지!##
                path.pop()  # pop해줘야지!! 백하는거니까!
                ch[i] = 0


if __name__=="__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1  # 방향그래프
    cnt = 0
    path = []  # 경로 저장할 리스트
    path.append(1)
    ch[1] = 1  # 1번노드 방문했다 하고 넘어감
    DFS(1)
    print(cnt)
