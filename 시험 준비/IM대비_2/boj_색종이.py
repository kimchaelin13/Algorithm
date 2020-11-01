import sys
sys.stdin=open('input.txt','r')
'''
이건 도움없이 풀었다
100*100 배열 만들고, 
3장안에서 읽어줘야 함.

행,열 읽어주면서 그냥 1로 다 바꿔줌(해당범위면)
'''

board=[[0]*100 for _ in range(100)]

for _ in range(int(input())):
    r,c=map(int,input().split())

    for i in range(r,r+10):
        for j in range(c,c+10):
            board[i][j]=1

cnt=0
for x in range(100):
    for y in range(100):
        if board[x][y]==1:
            cnt+=1
print(cnt)

