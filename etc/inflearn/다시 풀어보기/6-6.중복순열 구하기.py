import sys
sys.stdin=open('input.txt','r')

'''
3 2 
#1. res=[0,0,0] 짜리 만들고
#2. 만약에 res의 길이까지 가면 종료하고
#3. 아니면, res[L]=1하고, 


아니 나이거 순열이랑 부분집합 구하는거에서 ㅈㄴ헷갈리기시작함 뭐지???? => 상태트리를 그려보면서 생각하자
'''
def dfs(L):
    global cnt
    if L==m:
        for j in range(m):
            print(result[j],end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            result[L]=i
            dfs(L+1)

if __name__ == '__main__':
    n,m=map(int,input().split())
    result=[0]*m
    cnt=0
    dfs(0)
    print(cnt)
