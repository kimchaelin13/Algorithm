import sys
sys.stdin=open('input.txt','r')

'''
#1 주어진 숫자를 몇번 더해야 일의자리가 나오는지 횟수를 구해야함
#2 결과로 나온 일의자리숫자가 3의 배수면 예스, 아니면 노


'''
N=int(sys.stdin.readline())
ANS=0
CNT=0
RES=''
end=0
if N < 10:
    if N % 3:
        RES = 'NO'
    else:
        RES = 'YES'
    end=1
if end==0:
    temp = N
    while True:
        ANS+=temp%10
        temp=temp//10
        if temp==0:
            CNT+=1
            if ANS<10:
                break
            else:
                temp=ANS
                ANS=0
    if ANS%3:
        RES='NO'
    else:
        RES='YES'

print(CNT,RES,sep='\n')
