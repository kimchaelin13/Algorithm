import sys
sys.stdin=open('input.txt','r')

for tc in range(1,int(input())+1):

    S=input()
    A=''
    for i in S[::-1]:
        if i=='q':
            A+='p'
        elif i=='p':
            A+='q'
        elif i=='d':
            A+='b'
        else:
            A+='d'
    print('#{} {}'.format(tc,A))
