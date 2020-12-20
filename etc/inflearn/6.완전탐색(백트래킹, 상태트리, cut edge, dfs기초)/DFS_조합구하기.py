import sys
sys.stdin = open("input.txt", "r")

def DFS(L,s):
    global cnt

    if L==m:
        for j in range(L):
            print(res[j],end=" ")
        cnt+=1
        print()

    else:
        for i in range(s


if __name__=="__main__":
    n,m=map(int,input().split())
    result=[0]*(n+1)
    cnt=0
    DFS(0,1)