'''
중복없는 수열
n=3, m=2면
중복없이
1,2,3까지 2개씩 뽑아서 나열!
그럼 result배열을 만들고,check만들어서,다시 백했을때 체크를
풀어주도록 해야함
'''
import sys
sys.stdin = open("input.txt", "r")
def DFS(L):
    if L==m:
        for j in range(L):
            print(res[j],end=" ")
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0
if __name__ == "__main__":
    n,m=map(int,input().split())
    res=[0]*n
    ch=[0]*(n+1)
    DFS(0)