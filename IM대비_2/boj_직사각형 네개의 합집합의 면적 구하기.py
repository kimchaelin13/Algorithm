import sys
sys.stdin=open('input.txt','r')

'''
보드를 1로 채우는 생각
(1,2) (4,4)면 6칸이 색칠되야 함
그러면 좌푯값과 달리 4-1 * 4-2 를 하면 3*2=6으로 색칠됨! 내 생각이 맞음

for i in range(1,4):
    for j in range(2,4):
        board[i][j]=1 이생각이 중요함
'''
board=[[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j]=1

res=0
for i in range(100):
    for j in range(100):
        if board[i][j]==1:
            res+=1
print(res)
