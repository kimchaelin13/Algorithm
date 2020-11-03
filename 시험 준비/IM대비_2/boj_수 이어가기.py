'''
given = 100
cnt만 세야하는게아니라 요소도 모두 뽑아야하니까 저장해야한다는 생각을 해야한다
리스트를 만들어넣고 저장해보자

최대길이 리스트를 구해야하니까 일단 변수로 최소로

1~99까지 검사하면서, cnt를 세준다
뭔가 while로 해야할거같다.


res=-1234
result=[]
for i in range(1,100):
    temp=[n,i]
    while True:
        a=temp[-2]-temp[-1]
        temp.append(a)
        if a < 0:
            break

        if len(temp)>res:
            res=len(temp)
            result = temp[:]


'''

import sys
sys.stdin=open('input.txt','r')


res=-1234
result=[]

n=int(input())
for i in range(n+1): #0부터 100까지, 문제를 잘보시오
    temp=[n,i]
    while True:
        a=temp[-2]-temp[-1]
        temp.append(a)
        if a<0:
            break
        if len(temp)>res:
            res=len(temp)
            result = temp[:]
print(res)
print(*result)