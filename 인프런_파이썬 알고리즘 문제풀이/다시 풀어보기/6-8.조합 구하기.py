import sys
sys.stdin=open('input.txt','r')
'''
상태트리를 그려도 ㅈㄴ헷갈린다 진짜 시발 ㅠㅠ 
'''
def dfs(L,s):
    if L==M:
        for j in range(M):
            print(res[j],end=" ")
        print()
    else:
        for i in range(s,N+1):
            res[L]=i
            dfs(L+1,i+1)

if __name__ == '__main__':
    N,M=map(int,input().split())
    res=[0]*M
    dfs(0,1)