import sys
sys.stdin=open('input.txt','r')

'''
'''
def changetotwo(ten):
    for i in range(4):
        if ten & (8>>i):
            print('1',end="")
        else:
            print('0',end= "")

for tc in range(1,int(input())+1):
    N,S=input().split()
    N=int(N)
    print('#{}'.format(tc),end=" ")
    for i in range(N):
        #16
        ten=int(S[i],16)
        changetotwo(ten)
    print()

changetotwo(0.625)