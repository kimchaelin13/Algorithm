import sys
sys.stdin=open('input.txt','r')

'''
5 3
2 4 5 8 12
6


'''

def dfs(L,s,total):
    global cnt
    if L==K:
        if total%6==0:
            cnt+=1
    else:
        for i in range(s,N):
            dfs(L+1,i+1,total+nums[i])


if __name__ == '__main__':
    N,K=map(int,input().split())
    nums=list(map(int,input().split()))
    M=int(input())
    cnt=0
    dfs(0,0,0)
    print(cnt)