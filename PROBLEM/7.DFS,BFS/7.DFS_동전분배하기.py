import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global res
    # n이 되면 마지막 종착점,
    # 답을 구하는 코드가 if문 아래 써져있어야 하고
    if L==n:
        cha = max(money)-min(money)
        if cha<res: #차가 res보다 작을때
            # 이때 또 머니에 있는 세개의 돈이 달라야함
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                #그랬을때 res에 cha를 넣어준다
                res=cha
    else:
        #가지가 뻗어나가야한다. 세갈래이다. 사람이 세명이니까
        for i in range(3):
            #L번째있는 코인을 i번째 사람한테 주는거다
            money[i]+=coin[L]
            DFS(L+1)
            ##깊이 들어갔다가 다시 백을 하자, 전상황으로,
            # money[i]+=coin[L](돈을더했던 상황)을 백을 해주자
            money[i]-=coin[L]


if __name__ == '__main__':
    n=int(input())
    coin=[]
    money=[0]*3
    res=987654321
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
