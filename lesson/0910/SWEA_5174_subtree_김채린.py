import sys
sys.stdin = open("input.txt", "r")
def DFS(L):
    global cnt
    cnt+=1

    #노드안에 담겨있는 값이 있으면!! 자식노드가 있다는 뜻!!
    for i in tree[L]:
        print(i)
        #if i:
        DFS(i)

for tc in range(1,int(input())+1):
    E,N=map(int,input().split())
    temp=list(map(int,input().split()))
    tree=[[] for _ in range(E+2)]

    for i in range(0,len(temp),2):
        tree[temp[i]].append(temp[i+1])
    cnt=0
    DFS(N)
    print('#{} {}'.format(tc,cnt))
