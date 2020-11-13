import sys
sys.stdin=open('input.txt','r')

'''
9
1 2 2 4 4 5 7 7 2

클때 작을때 함수 따로 만들어서 체크하고
더 큰값을 리턴한다

'''
def increase(i):
    res=0
    if arr[i] <= arr[i+1]:
        cnt+=1


def decrease(i):
    
N=int(input())
arr=list(map(int,input().split()))
for i in range(N):
    increase(i)
    decrease(i)