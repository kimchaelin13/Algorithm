import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[L],end=" ")
        print()
        cnt+=1

    else:#뻗어나가자
        #뻗어나갈땐? 이렇게!
        for i in range(1,n+1):#1부터 n까지 돌아야하니까

            res[L]=i
            DFS(L+1)



if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0  # 개수출력
    DFS(0)