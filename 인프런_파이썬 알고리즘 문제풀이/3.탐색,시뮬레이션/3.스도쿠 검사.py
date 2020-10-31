import sys
sys.stdin=open('input.txt','r')

board=[list(map(int,input().split())) for _ in range(9)]
flag=1

#가로
for i in range(9):
    r=set()
    for j in range(9):
        r.add(board[i][j])
    if len(r) != 9:
        flag=0
        break

#세로
c=set()
for i in range(9):
    c = set()
    for j in range(9):
        c.add(board[i][j])
    if len(c) != 9:
        flag=0
        break

#3*3
for i in range(0,9,3):
    for j in range(0,9,3):
        s=set()
        for m in range(3):
            s.update(board[i+m][j:j+3])
        if len(s)!=9:
            flag=0
            break
if flag==1:
    print('yes')
else:
    print('no')