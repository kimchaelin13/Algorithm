import sys
sys.stdin=open('input.txt','r')

'''

'''

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
largest=-1234567

#행과 열의 합 구하기
for i in range(n):
    s1=s2=0
    for j in range(n):
        #고정되는건 어쨌든 i인거임
        s1+=board[i][j]
        s2+=board[j][i]
    if s1>largest:
        largest=s1
    if s2>largest:
        largest=s2

#대각선 합 구하기
s1=s2=0
for i in range(n):
    s1+=board[i][i]
    s2+=board[i][n-i-1]
if s1>largest:
    largest=s1
if s2>largest:
    largest=s2
print(largest)
