import sys
sys.stdin=open('input.txt','r')

'''
빙고 - 2차원 배열
사회자 - 1차원 배열로 만듦

사회자 콜 한개씩 읽으면서,
빙고에 있는 거 다 탐색하면서 같은거 찾으면 0으로 바꾼다(빙고숫자는 항상 0보다 큼)

그리고 그때 가로합, 세로합, 대각선합이 0보다 큰게 3개이상이 되면? 그때 스탑하고, 그때의 사회자콜 출력한다
'''
def check():
    ans=0

    #가로
    for k in range(5):
        if sum(bingo[k][:]) == 0:
            ans+=1

    #세로
    for j in range(5):
        temp=0
        for i in range(5):
            temp += bingo[i][j]
        if temp == 0:
            ans +=1

    #대각선
    temp_2=0
    for i in range(5):
        temp_2 += bingo[i][i]
    if temp_2 == 0:
        ans+=1
    temp_3=0
    for d in range(5):
        temp_3 += bingo[d][4-d]
    if temp_3==0:
        ans+=1

    return ans


bingo=[list(map(int,input().split())) for _ in range(5)]
call=[]
for _ in range(5):
    call.extend(list(map(int,input().split())))

ans=0
s=0
res=0
for c in range(s,25):
    flag=0
    for i in range(5):
        for j in range(5):
            if call[c] == bingo[i][j]:
                s+=1
                bingo[i][j]=0

                if check() >= 3 :
                    res = c+1
                    print(res)
                    flag=1
                    break
        if flag:
            break
    if flag:
        break
