import sys
sys.stdin=open('input.txt','r')

'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
'''

for tc in range(1,int(input())+1):
    N=int(input())
    selling_price = list(map(int,input().split()))
    MAX=selling_price[-1] #MAX 초기값 설정
    res=0
    for i in range(N-1)[::-1]:
        if selling_price[i] < MAX:
            res+=MAX-selling_price[i]
        else:
            MAX=selling_price[i]
    print('#{} {}'.format(tc,res))
