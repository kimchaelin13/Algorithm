import sys
sys.stdin=open('input.txt','r')

'''
#1. 5의 배수가 아니면 3을 빼고, cnt+1
    값이 2보다 작으면 -1
'''


n=int(input())
res=0
while True:
    if n%5!=0:
        if n<=2:
            result=-1
            break
        n=n-3
        res+=1
    else:
        res+=n//5
        break
print(res)