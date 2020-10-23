import sys
sys.stdin=open('input.txt','r')

'''
57 2

temp=[]

단순히 계산한것을 D 리스트에 넣다가, 중복이 나오면 그만두는 알고리즘으로 더 직관적이다.

#1. d리스트 만들기
계산한걸 D리스트에 넣는데, 계산한게 똑같은게 나오면 break해서 거기서 멈춤

#2. 전체에서 반복수열 제거하면 몇개남나? => d수열의 마지막에 연산을 하면! 어떤 숫자가 나오는데, 반복수열이기 때문에 그게 몇번 인덱스인지? 찾으면 
    그 0부터 그 인덱스전까지는 반복수열아닌 값들만 남겨짐
'''
#1
A,P=map(int,input().split())
D=[A]
i=0

while True:
    tempList = list(str(D[i]))
    #print(tempList)
    temp=0
    for x in tempList:
        temp+=int(x)**P
    if D.count(temp) > 0:
        break
    else:
        D.append(temp)
    i+=1

#2
tempList=list(str(D[-1]))
temp=0
for x in tempList:
    temp+=int(x)**P
print(D.index(temp))