import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    if L==m:
        for j in range(L):
            print(result[j],end=" ")
        print()

    else:
        for i in range(1,n+1):
            if check[i]==0:
                check[i]=1
                result[L]=i
                DFS(L+1)
                check[i]=0

#if __name__=="__main__":
n,m=map(int,input().split())
result=[0]*n
check=[0]*(n+1)
DFS(0)
