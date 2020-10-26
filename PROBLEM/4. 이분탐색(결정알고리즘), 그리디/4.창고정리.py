import sys
sys.stdin=open('input.txt','r')

'''
#내가 푼 방법
10
69 42 68 76 40 87 14 65 76 81
50

#1.리스트를 받고, sort해서 오름차순 정렬
#2.for i in range(50):
    list[0]+=1
    list[-1]-=1
    sorted(list)
#3.그다음에 list[-1]-list[0]
'''
N=int(input())
stocks=list(map(int,input().split()))
stocks.sort()

for i in range(int(input())):
    stocks[0]+=1
    stocks[-1]-=1
    stocks.sort()
print(stocks[-1]-stocks[0])


