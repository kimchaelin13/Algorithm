import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    cards=input()
    flag=1
    S, D, H, C = [],[],[],[]

    for i in range(0,len(cards),3):
        if cards[i] == 'S':
            #지금 [i:i+3]이 S리스트 안에 이미 중복되어있으면 안됨
            if cards[i:i+3] not in S:
                S.append(cards[i:i+3])
            #근데 만약에 중복되어 있는게 들어오면? error!!
            else:
                flag=0
                break

        elif cards[i] == 'D':
            if cards[i:i+3] not in D:
                D.append(cards[i:i+3])
            else:
                flag=0
                break

        elif cards[i]=='C':
            if cards[i:i+3] not in C:
                C.append(cards[i:i+3])
            else:
                flag=0
                break

        elif cards[i]=='H':
            if cards[i:i+3] not in H:
                H.append(cards[i:i+3])
            else:
                flag=0
                break

    if flag==1:
        print('#{} {} {} {} {}'.format(tc,13-len(S),13-len(D),13-len(H),13-len(C)))
    else:
        print('#{} ERROR'.format(tc))

