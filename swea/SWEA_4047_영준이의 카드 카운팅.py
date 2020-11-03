'''
영준이의 카드 카운팅

영준이가 받은 카드가 문자열로 주어질때, 영준이가 받지 않은 나머지 카드가 몇개 존재하는지 구하는 문제!!
'''

import sys
sys.stdin = open("input.txt", "r")

test = int(input())

for tc in range(1, test + 1):
    card = input()
    flag = 1
    s = []
    d = []
    h = []
    c = []

    for i in range(0, len(card), 3):
        if card[i] == 'S':
            #근데 그 똑같은 카드가 없어야됨.없으면 append
            if card[i:i + 3] not in s:
                s.append(card[i:i + 3])
            #중복카드있으면 flag=0해주고 break
            else:
                flag = 0
                break
        elif card[i] == 'D':
            if card[i:i + 3] not in d:
                d.append(card[i:i + 3])
            else:
                flag = 0
                break
        elif card[i] == 'H':
            if card[i:i + 3] not in h:
                h.append(card[i:i + 3])
            else:
                flag = 0
                break
        elif card[i] == 'C':
            if card[i:i + 3] not in c:
                c.append(card[i:i + 3])
            else:
                flag = 0
                break

    if flag==1:
        print(f'#{tc} {13 - len(s)} {13 - len(d)} {13 - len(h)} {13 - len(c)}')
    else:
        print(f'#{tc} ERROR')