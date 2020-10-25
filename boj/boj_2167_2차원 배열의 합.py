'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3

1.배열 입력받기
2.여기서 0으로 채워서 인덱스 맞춰줘야 함
3.k만큼 for문을 반복, (i,j) (x,y) 해서 더하면 되는거 아닌가, 여기서도 범위주의



#시간초과, dp로 푸는 문제였다........k가 엄청 많아지면 시간초과나는 문제다
import sys
sys.stdin=open('input.txt','r')
#1. 입력
N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
# print(arr)

#2. 인덱스 맞춰주기 작업
arr.insert(0,[0]*(M))
for x in arr:
    x.insert(0,0)
#print(arr)

#3.k만큼 for문을 반복
K=int(input())
for _ in range(K):
    ans=0
    i,j,x,y=map(int,input().split())

    for r in range(i,x+1):
        for c in range(j,y+1):
            ans+=arr[r][c]
    print(ans)

#dp로 풀자
'''

'''
1.memoization으로 테이블을 만들어놓는다
2.그리고 i,j,x,y 입력받고, 찾아놓은 규칙을 통해서 구한다
'''
import sys
sys.stdin=open('input.txt','r')

#1.입력받고, 0으로 채워주기
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
arr.insert(0,[0]*M)
for x in arr:
    x.insert(0,0)

#2.memoization 만듦
memo=[[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        memo[i][j]=arr[i][j]+memo[i-1][j]+memo[i][j-1]-memo[i-1][j-1]
#print(memo)

#3.i,j,x,y 받아서 답을 출력하자
K=int(input())
for _ in range(K):
    i,j,x,y=map(int,input().split())
    answer=memo[x][y]-memo[i-1][y]-memo[x][j-1]+memo[i-1][j-1]
    print(answer)