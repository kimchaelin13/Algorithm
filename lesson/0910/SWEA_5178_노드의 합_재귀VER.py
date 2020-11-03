import sys
sys.stdin = open("input.txt", "r")


# def DFS(V):
#     global result
#
#     #이게 종료조건이고
#     if V>N:
#         return
#     #여기서 프린트할거임
#     if tree[L] != 0:
#         result=tree[L]
#         return
#     else:
#         tree[V]=DFS(V*2)+DFS(V*2+1)
#         return
#
#
# for tc in range(1,int(input())+1):
#     N,M,L=map(int,input().split())
#     tree=[0]*(N+1)
#
#     #여기에 채우고
#     for _ in range(M):
#         a,b=map(int,input().split())
#         tree[a]=b
#     result=DFS(L)
#



def DFS(L):
    global result
    #종료조건, 궁금한거 왜 -1하니까 끝나지 뭐야 ;
    if L>N:
        return 0
    #만약에 tree[L]가 0이 아닌거면 멈추고 종료
    if tree[L] !=0:
        return tree[L]

    #채우기 재귀로,,,근데 이거 왜 돌아가? ㅋㅎㅋㅎ
    else:
        left=L*2
        right=L*2+1
        #
        tree[L]=DFS(left)+DFS(right)
        return tree[L]

for tc in range(1,int(input())+1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)

    #주어진 정보로 트리 채우고
    for _ in range(M):
        a,b=map(int,input().split())
        tree[a]=b

    result=DFS(L)
    print('#{} {}'.format(tc,result))
