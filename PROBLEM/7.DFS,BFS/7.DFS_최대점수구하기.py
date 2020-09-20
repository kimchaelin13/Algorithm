import sys
sys.stdin = open("input.txt", "r")

def DFS(L,sum,time):
    global result

    if time>m:
        return #가지치기
    if L==n:
        if sum>result:
            result=sum

    else:
            DFS(L+1,sum+pv[L],time+pt[L])
            DFS(L+1,sum,time)


if __name__ == "__main__":
    n,m=map(int,input().split())
    pv=[] #배점
    pt=[] #시간
    for i in range(n):
        a,b=map(int,input().split())
        pv.append(a)
        pt.append(b)
    result=-987654321 #최대를 구할거니까
    DFS(0,0,0)


