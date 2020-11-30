import sys
sys.stdin=open('input.txt','r')

'''

'''

for tc in range(1,int(input())+1):
    price=list(map(int,input().split()))
    #print(price)
    bind=0
    for i in range(3):
        if price[i]>=50:
            price[i]-=10
        else:
            bind+=price[i]
            price[i]=0
    if bind>=50:
        bind=bind-10
    res=sum(price)+bind
    print('#{} {}'.format(tc,res))