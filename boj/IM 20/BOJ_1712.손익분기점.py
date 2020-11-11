import sys
sys.stdin=open('input.txt','r')

A,B,C=map(int,sys.stdin.readline().split())
if (C-B) <= 0:
    print('-1')
else:
    n=(A//(C-B))+1
    if n<=0:
        print('-1')
    else:
        print(n)