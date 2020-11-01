import sys
sys.stdin=open('input.txt','r')

'''
100*100 배열에 채움

그리고 가장 왼쪽행을 읽으면서 1이 있는 좌표부터 맨 끝 좌표까지 다 더함 

'''

#
# def count():
#
#     cnt=sum(board[j][i:max_r+1])



board=[[0]*100 for _ in range(100)]
N=int(input())

max_r=0
max_h=0
for _ in range(N):
    a,b=map(int,input().split())

    for i in range(1,b+1):
        board[a][i] = 1
    if a>max_r:
        max_r=a
    if b>max_h:
        max_h=b
# 2. 1열씩 위에서 읽으면서 1이 있는데부터 1이 끊기는데까지 모두 더한다.
ans=0
tmp=0
for i in range(100):
    for j in range(100):
        if board[j][i] == 1:
            #열을 읽다가, 1을 찾으면? 1이 더이상 아닐때까지 다 더함! 그 열을 다 더해주는 함수, 거기서 다 더하면 ans에 추가하고 다음 열로 넘어갈것
            tmp = sum(board[j][i:max_r + 1])
            ans += tmp
print(ans)

