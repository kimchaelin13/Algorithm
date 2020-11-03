import sys
sys.stdin = open("input.txt", "r")


def DFS(L,P):
    global cnt
    if L==n: #길이가 되면 종착점에 온것
        cnt+=1 #개수가 하나 완성된것

    else:
        for i in range(1,27):
            if code[L] == i:
                res[P]=i
                DFS(L+1,P+1)
            elif i>=10 and code[L]==: #두자리숫자일때



if __name__=='__main__':
    code=list(map(int,input()))
    n=len(code) #n이 종착점
    #code.insert(n,-1) #
    res=[0]*(n+3)
    cnt=0
    DFS(0,0)