import sys
sys.stdin=open('input.txt','r')

'''
i=0따로 
i=1,i=2 => i=0일때의 별 개수 - (L은 1개, R 1개니까) => i=1, 공백 9


전체 len=> 4(N-1)+1 (4가 공차인 등차수열을 이룬다)

i=0
i=1 (L,R 각각1개)
i=2 
i=3 (L +2 R+2_
i=4
'''


N=int(input())
L_star='* '
R_star=' *'

L=4*(N-1)+1
print(L)
L_CNT,R_CNT,EMPTY_CNT=1,1,L-4
for i in range(L):
    #i가 7이 되면 => 5로 바꿔줌
    if i >= L//2+1:
        i = (L-1)-i
        L_CNT -=1
        R_CNT -=1
        EMPTY_CNT += 4
    if i==0:
        print('*'*L)
    #홀수일때는 공백이 출력되고
    if i%2!=0:
        print(L_star * L_CNT + ' '*EMPTY_CNT + R_star * R_CNT)
    #짝수일때는 별이 출력된다
    elif i!=0 and i%2==0:
        print(L_star * L_CNT + '*' * EMPTY_CNT + R_star * R_CNT)
        L_CNT +=1
        R_CNT +=1
        EMPTY_CNT -=4