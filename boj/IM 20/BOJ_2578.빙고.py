import sys
sys.stdin=open('input.txt','r')


'''
한글자씩 하고.

한글자 지우고 나면 -> 체크 가로 세로 대각선 다 체크해서 빙고되면 -> +1

+3 => 멈추고 그때 수 저장해서 출력한다

'''
'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
bingo = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]
# print(bingo)
# print(call)

def check():    #가로,세로, 대각선에 -1로 이뤄진 선이 있는지 확인
    lcnt = 0    #라인의수
    for i in range(5):  #가로방향
        cnt = 0 #-1의 수, 열의 위치
        while cnt <5 and bingo[i][cnt] == -1 :
            cnt+=1
        if cnt == 5:
            lcnt+=1
    for i in range(5):  #세로방향
        cnt = 0 #-1의 수, 열의 위치
        while cnt <5 and bingo[cnt][i] == -1 :
            cnt+=1
        if cnt == 5:
            lcnt+=1
    #대각선방향 카운팅
    while cnt <5 and bingo[cnt][cnt] == -1 :
        cnt+=1
    if cnt == 5:
        lcnt+=1
    while cnt <5 and bingo[4-cnt][cnt] == -1 :
        cnt+=1
    if cnt == 5:
        lcnt+=1
    return lcnt
isBingo = False    #빙고인지 아닌지를 저장
ncnt = 0    #숫자를 외치는 횟수
for i in range(5):
    for j in range(5):
        # print(call[i][j])
        ncnt +=1
        for k in range(5):
            for m in range(5):
                if bingo[k][m] == call[i][j]:
                    bingo[k][m] = -1
        if check() >= 3:
            isBingo = True
    if isBingo: break
print(ncnt)

# def hor_ver_check(arr):
#     total_hor_ver=0
#
#     for i in range(10):
#         if sum(arr[i][:]) == 0:
#             total_hor_ver+=1
#     return total_hor_ver
#
# def dia_check(arr):
#     total_dia=0
#     TEMP=0
#     for i in range(5):
#         TEMP += arr[i][i]
#     if TEMP==0:
#         total_dia +=1
#
#     # total_dia=0
#     TEMP=0
#     for i in range(5):
#         TEMP += arr[i][4-i]
#     if TEMP == 0:
#         total_dia +=1
#
#     return total_dia
#
# #빙고판
# arr=[list(map(int,input().split())) for _ in range(5)]
#
# #사회자 call
# call=[]
# for _ in range(5):
#     call.extend(map(int,input().split()))
#
# ans=0
# s=0
# flag=0
# for i in range(s,len(call)):
#     #print(s)
#     for r in range(5):
#         for c in range(5):
#             #print(s)
#             if call[s] == arr[r][c]:
#                 arr[r][c] = 0
#                 temp = arr + list(zip(*arr))
#
#                 hor_ver_check(temp)
#                 dia_check(arr)
#
#                 if hor_ver_check(temp)+dia_check(arr)>=3:
#                     print(s+1)
#                     flag=1
#                     break
#         if flag:
#             break
#     if flag:
#        break
#
#     s+=1