import sys
sys.stdin=open('input.txt','r')

'''
5 0
-7 -3 -2 5 8

#1.n,s입력받고/nums 리스트 입력받음
#2.dfs(0,0)으로 시작해서 재귀로 하다가, 만약에 레벨 끝까지 갔는데 total==0이면, 그때 cnt+=1
'''


def dfs(L,total):
    global cnt
    # if total>S:
    #     return

    if L==N:
        if total==S:
            cnt+=1

    else:
        dfs(L+1,total+nums[L])
        dfs(L+1,total)

N,S=map(int,input().split())
nums=list(map(int,input().split()))
cnt=0
dfs(0,0)
#아무것도 선택하지 않았을때(공집합)은 제외시켜야함 => cnt-1
if S==0:
    print(cnt-1)
else:
    print(cnt)