import sys
sys.stdin=open('input.txt','r')

'''
n=3으로 입력이 들어오면 
1
2
3
12 13 23
123

다 뽑아야 한다.

#1. res배열 (N+1)짜리만들고
#2. L=0부터 시작해서 L==N+1가 되면 종료하고, res안에 1로 체크되있으면 그 인덱스를 뽑는다
#3. res배열을 1부터! n+1까지 탐색하면서
    그자리를 선택하고,res[L]=1
    DFS(L+1)
    res[L]=0
    DFS(L+1) **이걸 빼먹음.아직 잘 모르는듯 
'''

def dfs(L):
    if L==N+1:
        for j in range(1,N+1):
            if res[j]==1:
                print(j,end=' ')
        print()

    else:
        res[L]=1
        dfs(L+1)
        res[L]=0
        dfs(L+1)

if __name__ == '__main__':
    N=int(input())
    res=[0]*(N+1)
    dfs(1)