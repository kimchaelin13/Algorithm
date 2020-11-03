import sys
sys.stdin=open('input.txt','r')
'''

'''
N=int(input())
MAX=0
for _ in range(N):
    score=0
    a1,a2,a3=map(int,input().split())
    if (a1==a2) and (a2==a3):
        score=10000+(a1*1000)
    elif (a1 != a2) and (a2 != a3) and (a3 != a1):
        score=max(a1,a2,a3)*100
    elif (a1 == a2):
        score=1000+(a1*100)
    elif (a1 == a3):
        score=1000+(a1*100)
    elif (a2==a3):
        score=1000+(a2*100)

    if score>MAX:
        MAX=score
print(MAX)
