import sys
sys.stdin = open("input1.txt", "r")

'''
회문
문제좀 똑바로 읽자 
N*N행렬에서 M길이짜리 펠린드롬을 찾는것임
'''

#가로줄을 확인할거야
#우선 가로줄로 먼저 받고, 그 각각 요소를 슬라이싱해서 같은지 확인한다.

# for tc in range(1,int(input())+1):
#     n,m = map(int,input().split())
#     result=[]
#
#     #가로줄 체크
#     garo = [input() for _ in range(n)]
#     for ga in garo:
#         for j in range(n-m+1):
#             if ga[j:j+m] == ga[j:j+m][::-1]:
#                 result.append(ga[j:j+m])
#
#     #세로줄 체크
#     #먼저 sero를 만들어야한다
#     sero = []
#     sero_sub =''
#     for i in range(n):
#         for ga in garo:
#             sero_sub += ga[i]
#         sero.append(sero_sub)
#         sero_sub = ''
#     #print(sero)
#
#     #세로줄 체크
#     for se in sero:
#         for j in range(n-m+1):
#             if se[j:j+m] == se[j:j+m][::-1]:
#                 result.append(se[j:j+m])
#     #print(f'#{tc} {result[0]}')
#     print('#{} {}'.format(tc, result[0]))

'''
일단 그 행렬을 받아서 
가로줄에서 펠린드롬이 있는지 찾고, 앞과 뒤를 비교하고, 저장해놓음(근데 비교할때, 주어진 길이만큼 짤라서 읽기)
세로줄은 지금 만들어야됨. 세로줄을 가로줄처럼 눕혀서 만들고, 가로줄이랑 똑같이 진행하자
'''

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    garo = [input() for _ in range(n)]
    result = []
    for ga in garo:
        for i in range(len(ga)-m+1):
            if ga[i:i+m] == ga[i:i+m][::-1]:
                result.append(ga[i:i+m])


    sero=[]
    sero_sub=''
    for i in range(n):
        for ga in garo:
            sero_sub += ga[i]
        sero.append(sero_sub) #위치
        sero_sub=''

    for se in sero:
        for i in range(len(se)-m+1):
            if se[i:i+m] == se[i:i+m][::-1]:
                result.append(se[i:i+m])
    print('#{} {}'.format(tc,result[0]))


#선생님풀이
def check():
    #전체 크기가 N
    for i in range(N):
        #가로 검사
        for j in range(N-M+1):
            tmp = words[j][j:j+M]
            if tmp == tmp[::-1]:
                return tmp
        #세로 검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == tmp[::-1]:
                return tmp
    return []

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    words=[list(input()) for _ in range(N)]
    ans=check()

    print("#{} {}".format(tc, ''.join(ans)))

