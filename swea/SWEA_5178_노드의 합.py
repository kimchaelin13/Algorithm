import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global result
    if L>n:
        return
    if fulltree[l] !=0:
        result=fulltree[l]
        return
    else:
        fulltree[L]=DFS(L*2)+DFS(L*2+1)

for tc in range(1,int(input())+1):
    n,m,l=map(int,input().split())
    fulltree=[0]*(n+1)
    for _ in range(m):
        n,v=map(int,input().split())
        fulltree[n]=v
    #print(fulltree)
    result=0
    DFS(l)