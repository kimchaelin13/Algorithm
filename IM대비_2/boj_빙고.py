import sys
sys.stdin=open('input.txt','r')

def check():
    cnt=0
    #가로세로확인
    for i in range(N):
        cnt_row=0
        cnt_col=0
        for j in range(N):
            if bingo[i][j] == 0: cnt_col += 1
            if bingo[j][i] == 0: cnt_row +=1
        if cnt_row == N: cnt+=1
        if cnt_col == N: cnt+=1

    cnt_l=0
    cnt_r=0
    for i in range(N):
        if bingo[i][i]==0: cnt_l+=1
        if bingo[i][N-1-i]==0: cnt_r+=1
    if cnt_l==N:cnt+=1
    if cnt_r==N:cnt+=1

    if cnt>=3: return True
    return False
N=5
bingo=[list(map(int,input().split())) for _ in range(N)]

#해당 번호 좌표 담기
pos = [0]*26
for i in range(N):
    for j in range(N):
        pos[bingo[i][j]] = (i,j)


#사회자가 호출하는 번호 한줄로 만들기
call=[]
for i in range(N):
    call += list(map(int,input().split()))

ans = 0

while not check():
    r,c=pos[call[ans]]
    print((r,c))
    bingo[r][c] = 0
    ans+=1
print(ans)





'''
선생님이 부르는거대로 0으로 지워나갈것임
0 하나를 지우고 나면 -> 검사를 함

만약에 
sum(board[i][:])==0 이면 cnt+=1
sum(board[j][:])==0 이면 cnt+=1
sum(board[i][i])==0 이면 cnt+=1
sum(board[i][4-i]==0) 이면 cnt+=1

그리고 cnt가 3이 된다면? 멈추고, 그때의 n값을 res에 담는다. n은 쌤이 부른 그것
'''
'''
board=[list(map(int,input().split())) for _ in range(5)]
temp=[list(map(int,input().split())) for _ in range(5)]
nums=[]
for i in range(5):
    for j in range(5):
        nums.append(temp[i][j])

cnt=0
res=0

for n in range(len(nums)):
    for i in range(5):
        for j in range(5):

'''

