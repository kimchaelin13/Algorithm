import sys
sys.stdin=open('input.txt','r')

for _ in range(int(input())):
    A,B=map(int,input().split())

    MAX=0
    for i in range(1,min(A,B)+1):
        if (A%i==0) and (B%i==0):
            if i>MAX:
                MAX=i
    print((A//MAX)*(B//MAX)*MAX)