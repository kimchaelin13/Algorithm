import sys
sys.stdin=open('input.txt','r')


N=int(input())
star='*'+' '*(N-2)+'*'
length=N+(N-1)
M_EMPTY_CNT = 2*(N-2)+1
S_EMPTY_CNT = 1

M_STAR = '*'+' '* (N-2) + '*' + ' '*(N-2) +'*'

for i in range(length):
    if (N-1)>=i:
        if i==0:
            print('*'*N+' '*M_EMPTY_CNT+'*'*N)
            M_EMPTY_CNT -=2
        elif 0<i<(N-1):
            print(' '*S_EMPTY_CNT + star + ' '*M_EMPTY_CNT + star)
            S_EMPTY_CNT +=1
            M_EMPTY_CNT -= 2
        elif i==N-1:
            print(' '*S_EMPTY_CNT + M_STAR)

    elif (length-1)>i:
        S_EMPTY_CNT -=1
        M_EMPTY_CNT +=2
        print(' '*S_EMPTY_CNT + star + ' '*M_EMPTY_CNT + star)
    else:
        M_EMPTY_CNT = 2*(N-2)+1
        print('*'*N+' '*M_EMPTY_CNT+'*'*N)


