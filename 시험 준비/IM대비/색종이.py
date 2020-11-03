import sys
sys.stdin=open('input.txt','r')

'''
왼쪽 아래 좌표인 3,7이 정해지면 오른쪽 위쪽 좌표도 정해진다. -> (3,7) (13,17)
이런식 그러면 보드 100*100을 만들고
3,7을 받고, 범위 설정은 (3,10+3) 하면서 돌아준다 ㅇㅋ
'''

board=[[0]*102 for _ in range(102)]
n=int(input())

for _ in range(n):
    x1,y1=map(int,input().split())

    for i in range(x1,x1+10):
        for j in range(y1,y1+10):
            if board[i][j]==0:
                board[i][j]=1

ans=0
for i in range(102):
    for j in range(102):
        if board[i][j]==1:
            ans+=1
print(ans)
