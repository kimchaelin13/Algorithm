import sys
sys.stdin=open('input.txt','r')

'''
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.


cnt변수가 필요하고,언제 다시 돌아올지 모르기 때문에 while문으로 처리해야다.

26 => 68 => 84

#1.

'''

N=int(input())
temp=N
NEXT=''
cnt=0
while True:
    cnt+=1
    NEXT += str(temp%10)
    NEXT += str(((temp//10)+(temp%10))%10)

    if int(NEXT) == N:
        break
    else:
        temp=int(NEXT)
        NEXT=''
print(cnt)