import sys
sys.stdin=open('input.txt','r')

'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3


9 9 5 6 5 6 1 1 4 2 2 1

p1 : 9,

'''


# D3 5203 베이비진 게임
def check(num, cardlist):
    pass

for tc in range(1,int(input())+1):
    player1 = [0]*10
    player2 = [0]*10
    card_list = list(map(int, input().split()))
    for i in range(12):
        #p2가 선택
        if i % 2:
            player2[card_list[i]] += 1
            # 체크
            check(2, card_list[i])
        #p1이 선택
        else:
            player1[card_list[i]] += 1
            # 체크
            check(1, card_list[i])
