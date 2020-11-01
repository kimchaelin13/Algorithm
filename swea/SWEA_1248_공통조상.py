import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    V,E,N,M=map(int,input().split())
    temp=list(map(int,input().split()))

    tree=[[] for _ in range(V+1)]

    #트리 채우기
    for i in range(0,len(temp),2):
        tree[temp[i]].append(temp[i+1])
    #print(tree)

    p1=0
    p2=0

    #N과 M의 공통조상을 찾을때까지 돌림
    #13이 몇번 인덱스에 있는지? 11번 INDEX, 그러면 11은 몇번에 있어? 6, 이런식으로 가고,
    #8은? 8은 몇번 index에 있어? 하면서
    for sub in tree:
        #print(sub)
        p1=sub.index(N)
        p2=sub.index(M)

