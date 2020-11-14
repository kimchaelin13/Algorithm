import sys
sys.stdin=open('input.txt','r')


'''
한글자씩 하고.

한글자 지우고 나면 -> 체크 가로 세로 대각선 다 체크해서 빙고되면 -> +1

+3 => 멈추고 그때 수 저장해서 출력한다

'''
def hor_ver_check(arr):
    global bingo

    for i in range(10):
        if sum(arr[i][:]) == 0:
            bingo+=1


def dia_check(arr):
    global bingo

    res=0
    for i in range(5):
        res += arr[i][i]
    if res==0:
        bingo +=1

    res=0
    for i in range(5):
        res += arr[i][4-i]
    if res==0:
        bingo+=1


#사회자 부르는 call 담기
call=[]
for _ in range(5):
    call.extend(map(int,input().split()))
#print(call)

#빙고
arr=[list(map(int,input().split())) for _ in range(5)]

temp = arr + list(zip(*arr))
#print(temp)


bingo=0
ans=0

s=0


for i in range(5):
    for j in range(5):
        if call[s] == arr[i][j]:
            arr[i][j] = 0
            hor_ver_check(zip(arr))
            dia_check(arr)

            if bingo==3:
                ans=arr[i][j]
                print(ans)
                break
            s+=1
