import sys
sys.stdin=open('input.txt','r')

'''
01110101
남자 -> 3번을 받으면, 배수에 해당하는 곳이 0->1, 1->0

여자 -> 3번을 받으면, (3-1)과 (3+1)을 비교 -> 둘이 같을때까지 계속 비교해야 함
                                                둘 값이 다르면 그때 break 하고
                                                어디부터 어디까지인지 저장
                                                만약에 (2,4)라면 (2~4)까지 바꿔주고
                                  
'''
'''
1.저는 size=2 되면 내려가게 하고 싶은데,,,,size=3까지 하고 내려가는데 어떻게 해줘야할지 모르겠어요
2.그래서 아래에서 -1빼서 해서 출력값은 나왔는데 런타임에러,,
'''

def male(bulb,start):
    for i in range(start,N+1,start):
        if bulb[i]==0:
            bulb[i]=1
        else:
            bulb[i]=0
    return bulb

def female(bulb,start):
    size=1
    while True:
        if (start - size <= 0 or start + size >= N + 1) or (bulb[start-size] != bulb[start+size]):
            break
        size+=1

    for i in range(start-size,start+size+1):
        if bulb[i]==1:
            bulb[i]=0
        else:
            bulb[i]=1
    return bulb

if __name__ == '__main__':
    N=int(sys.stdin.readline())
    bulb=list(map(int,sys.stdin.readline().split()))
    bulb.insert(0,0)
    number=int(sys.stdin.readline())

    for _ in range(number):
        gender,start=map(int,sys.stdin.readline().split())
        if gender==1:
            bulb=male(bulb,start)
            #print(bulb)
        else:
            bulb=female(bulb,start)

    for idx in range(1,len(bulb),20):
        print(*bulb[idx:idx+20])
