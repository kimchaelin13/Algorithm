import sys
sys.stdin = open("input.txt", "r")

def DFS(N):
    global cnt
    cnt+=1

    for i in fulltree[N]:
        DFS(i)

for tc in range(1,int(input())+1):
    E,N=map(int,input().split())
    temp=list(map(int,input().split()))
    fulltree=[[] for _ in range(E+2)]
    #print(fulltree)
    for i in range(0,len(temp),2):
        a=temp[i]
        b=temp[i+1]
        fulltree[a].append(b)
    cnt=0
    DFS(N)
    print('#{} {}'.format(tc,cnt))