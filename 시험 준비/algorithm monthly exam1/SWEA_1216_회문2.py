import sys
sys.stdin = open("input3.txt", "r")
from pprint import pprint

for tc in range(1,2):
    trash=input()
    result=1 #회문을 찾으면 result를 계속 갱신할것
    N=100
    #가로
    garo=[list(input()) for _ in range(100)]
    sero=list(zip(*garo))

    word = []
    word2 = []
    ans = 0
    result = 0
    for M in range(20,result,-1):
        flag = False
        for i in range(100):
            for j in range(100-M+1):
                word += garo[i][j:j+M]
                word2 += sero[i][j:j+M]
                if word == word[::-1] or word2 == word2[::-1]:
                    ans = M
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

    print(ans)

    #세로
    # sero=[]
    # for i in range(100):
    #     sero_sub = ''
    #     for ga in garo:
    #         sero_sub+= ga[i]
    #     sero.append(sero_sub)
    #
    #
    # #세로를 해보자~~~
    # for M in range(100,result,-1):
    #
    #     for se in sero:
    #         for i in range(N-M+1):
    #             if se[i:i+M] == se[i:i+M][::-1]:
    #                 if len(se[i:i+M])>result:
    #                     result=len(se[i:i+M])
    #     if result>M:
    #         break
    # print('#{} {}'.format(tc,result))


