import sys
sys.stdin=open('input.txt','r')
'''
.(s와 e는 2부터 9사이의 정수) 
'''
N,M=map(int,input().split())

if N<2 or N>9 or M<2 or M>9:
    print("INPUT ERROR!")
else:
    for i in range(1,10):
        print('{} * {} = {}'.format(N,i,N*i))