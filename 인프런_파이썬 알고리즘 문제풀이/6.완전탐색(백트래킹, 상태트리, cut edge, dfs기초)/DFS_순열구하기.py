import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j],end=" ")


    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n  # 여기 1,2/1,3 이런거할거고
    ch = [0] * (n + 1)
    cnt=0
    DFS(0)
    print(cnt)