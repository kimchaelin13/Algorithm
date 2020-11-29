import sys
sys.stdin=open('input.txt','r')

'''
최대공약수를 찾고 그걸로 나눠줌
'''
A,B=map(int,input().split(':'))

#최대공약수 구하기
MAX=0
for i in range(1,min(A,B)+1):
    if A%i==0 and B%i==0:
        if i>MAX:
            MAX=i
print(str(A//MAX)+':'+str(B//MAX))
