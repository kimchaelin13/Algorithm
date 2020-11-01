import sys
sys.stdin = open("input3.txt", "r")
'''

'''



# for tc in range(1, 11):
#     tc = int(input())
#     N = 100
#     result = 1
#
#     #가로줄 확인
#     garo=[input() for _ in range(100)]
#         #회문 길이
#     for M in range(N, result, -1):
#         if result > M:
#             break
#         for ga in garo:
#             for i in range(N-M+1):
#                 if ga[i:M+i] == ga[i:M+i][::-1]:
#
#                     if len(ga[i:M+i]) > result:
#                         result=len(ga[i:i+M])
#
#
#     #세로줄 확인
#     sero=[]
#     sero_sub=''
#     for j in range(100):
#         for ga in garo:
#             sero_sub+=ga[i]
#         sero.append(sero_sub)
#         sero_sub = ''
#
#     for se in sero:
#         for M in range(N, result, -1):
#             if result > M:
#                 break
#             for k in range(N-M+1):
#                 if se[k:M+k] == se[k:M+k][::-1]:
#                     if len(se[k:M+k]) > result:
#                         result = len(se[k:M+k])
#
#     print("#%d %s"%(tc, result))

#선생님 코드
#뒤에서부터 구하는게 편함?
#3칸짜리를 찾는게 가장 길다는 보장이 없어서 계속 늘려서 찾아야하는데
#애초에 제일 긴상태에서 확인하고, 그게 안되면 한칸 줄여서 확인하고, 이런식으로 찾다보면 더 효율적

# def check(K):
#     for i in range(N):
#         for j in range(N-M+1):
#             #가로
#             tmp = words[i][j:j+M]
#
#             #세로
#             tmp2 = zwords[i][j:j+M]
#
#             if tmp == tmp[::-1] or tmp2==tmp2[::-1]:
#                 return M
#     return 0
#
# for tc in range(10):
#     tc_num=int(input())
#     N=100 #100*100
#     words=[list(input()) for _ in range(N)]
#     zwords = list(zip(*words)) #2중리스트니까 언패킹, 하나 벗겨서 가져옴
#
#     for k in range(100,0,-1):
#         ans =check()
#         if ans!=0:
#             break
#     print("#{} {}".format(tc_num,ans))



for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1

    #가로줄 확인
    Garo_lst = []
    for i in range(N):
        Data = input()
        Garo_lst.append(Data)
        #회문 길이
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if Data[k:M+k] == Data[k:M+k][::-1]:
                    if len(Data[k:M+k]) > result:
                        result = len(Data[k:M+k])

    #세로줄 확인
    Sero_lst = []
    Sero_sub_lst = ''
    for x in range(N):
        for y in Garo_lst:
            Sero_sub_lst += y[x]
        Sero_lst.append(Sero_sub_lst)
        Sero_sub_lst =''

    for sero_data in Sero_lst:
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if sero_data[k:M+k] == sero_data[k:M+k][::-1]:
                    if len(sero_data[k:M+k]) > result:
                        result = len(sero_data[k:M+k])

    print(f'#{tc} {result}')