import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global num

    if L>N:
        return

    else:
        DFS(L*2)
        arr[L]=num
        num+=1
        DFS(L*2+1)

for tc in range(1,int(input())+1):
    N=int(input())#노드개수
    arr=[0]*(N+1) #노드개수만큼 빈리스트
    num=1
    DFS(1)
    print(arr)
    print('#{} {} {}'.format(tc,arr[1],arr[N//2]))



