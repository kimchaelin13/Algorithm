import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global num
    #종료조건
    if L>N:
        return
    else:
        DFS(L*2)
        tree[L]=num
        num+=1
        DFS(L*2+1)
for tc in range(1,int(input())+1):
    N=int(input())
    tree=[0]*(N+1)
    num=1
    DFS(1)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))
