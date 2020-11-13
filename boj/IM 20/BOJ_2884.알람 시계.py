import sys
sys.stdin=open('input.txt','r')

'''
분을 먼저 확인
(45분~59분) => 분에서 45분을 빼주고, 시는 그대로 출력한다
(0분~44분) => 60 - (45-x) = 분, 시는 -1를 하고 출력하는데(시가 0이면 23으로 출력한다) 
'''

H,M=map(int,input().split())
if 45<=M<=59:
    print(H,M-45)
else:
    M=60-(45-M)
    if H==0:
        H=23
    else:
        H-=1
    print(H,M)


h, m = map(int, input().split())
print((h+(m-45)//60)%24, (m-45)%60)