import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    result=[]
    #가로부터 먼저 검사
    garo=[input() for _ in range(N)]
    for ga in garo:
        for i in range(N-M+1):
            if ga[i:i+M]==ga[i:i+M][::-1]:
                result.append(ga[i:i+M])

    #세로는 세로 쪼개서 가로처럼 만들기 먼저해야함...
    sero=[]
    for i in range(N):
        sero_sub = ''
        for ga in garo:
            sero_sub+=ga[i]
        sero.append(sero_sub)

    #다 만들었다! 세로검사 시작~
    for se in sero:
        for i in range(N-M+1):
            if se[i:i+M]==se[i:i+M][::-1]:
                result.append(se[i:i+M])
    print('#{} {}'.format(tc,result[0]))