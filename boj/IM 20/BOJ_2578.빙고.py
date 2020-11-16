import sys
sys.stdin=open('input.txt','r')


'''
한글자씩 하고.

한글자 지우고 나면 -> 체크 가로 세로 대각선 다 체크해서 빙고되면 -> +1

+3 => 멈추고 그때 수 저장해서 출력한다

'''
def hor_ver_check(arr):
    total_hor_ver=0

    for i in range(10):
        if sum(arr[i][:]) == 0:
            total_hor_ver+=1
    return total_hor_ver

def dia_check(arr):
    total_dia=0
    TEMP=0
    for i in range(5):
        TEMP += arr[i][i]
    if TEMP==0:
        total_dia +=1

    # total_dia=0
    TEMP=0
    for i in range(5):
        TEMP += arr[i][4-i]
    if TEMP == 0:
        total_dia +=1

    return total_dia

#빙고판
arr=[list(map(int,input().split())) for _ in range(5)]

#사회자 call
call=[]
for _ in range(5):
    call.extend(map(int,input().split()))

ans=0
s=0
flag=0
for i in range(s,len(call)):
    #print(s)
    for r in range(5):
        for c in range(5):
            #print(s)
            if call[s] == arr[r][c]:
                arr[r][c] = 0
                temp = arr + list(zip(*arr))

                hor_ver_check(temp)
                dia_check(arr)

                if hor_ver_check(temp)+dia_check(arr)>=3:
                    print(s+1)
                    flag=1
                    break
        if flag:
            break
    if flag:
       break

    s+=1