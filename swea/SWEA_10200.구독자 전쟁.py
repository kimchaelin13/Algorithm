import sys
sys.stdin=open('input.txt','r')

'''
10 3 5 


#1. N >= (A+B) => 최대: 작은쪽 , 최소: 0
#2. N < (A+B) => 최대: 작은쪽, 최소: 10-(7+5)
#3. N=A=B, 최소 최대 모두 같음
'''

for tc in range(1,int(input())+1):
    N,A,B=map(int,input().split())
    MIN=0
    MAX=0
    #1.
    if N>=(A+B):
        MIN=0
        MAX=min(A,B)
    #2.
    elif N<(A+B):
        MIN=-(N-(A+B))
        MAX=min(A,B)
    elif (N==A) and (A==B):
        MIN=A
        MAX=A
    print('#{} {} {}'.format(tc,MAX,MIN))