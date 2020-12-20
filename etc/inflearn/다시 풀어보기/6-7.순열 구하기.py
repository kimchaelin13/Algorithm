import sys
sys.stdin=open('input.txt','r')


def dfs(L):
    if L==M:
        for j in range(M):
            print(res[j],end=" ")
        print()
    else:
        #이미 쓴 숫자면 뻗어나가면 안됨,,어떻게 해야하지? => check배열로 확인하자
        for i in range(1,N+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                dfs(L+1)
                ch[i]=0
            #r#s[L]=

if __name__ == '__main__':
    N,M=map(int,input().split())
    ch=[0]*(N+1)
    res=[0]*M
    dfs(0)