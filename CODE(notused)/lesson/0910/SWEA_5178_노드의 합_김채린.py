import sys
sys.stdin = open("input.txt", "r")


#여기서 tree를 다 채워줄거임...
def maketree(L):
    for i in range(len(tree)//2)[::-1]:
        left=i*2
        right=i*2+1

        if tree[left] and tree[right]:
            tree[i]=tree[left]+tree[right]

        elif tree[right]==0:
            tree[right]=tree[right*2]
            tree[i]=tree[left]+tree[right]


for tc in range(1,int(input())+1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)

    #주어진걸 tree에 채워넣었다..
    for _ in range(M):
        a,b=map(int,input().split())
        tree[a]=b
    maketree(1)
    print('#{} {}'.format(tc,tree[L]))






