import sys
sys.stdin=open('input.txt','r')

def DFS(L,S,B):
    global res
    if L==N:
        if res>abs(S-B):
            res=abs(S-B)

    else:
        DFS(L+1,S*ingre[L][0],B+ingre[L][1])
        DFS(L+1,S,B)

if __name__=='__main__':
    N=int(input())
    ingre=[]
    for _ in range(N):
        s,b=map(int,input().split())
        ingre.append((s,b))
    #print(ingre)
    res=987654321
    DFS(0,1,0)
    print(res)
