'''
100

36 33 이런거 판별할때 while을 써보자!
'''

N=int(input())
for i in range(1,N+1):
    #print(i,end=" ")
    n=i #숫자 저장
    is369=False #369인지 아닌지 판별하기 위한변수,flag
    #while로 판별해보자
    while n>0: #숫자가 0보다 큰동안 반복해
        d=n%10 #마지막 숫자 뜯어옴(1의 자리)
        n=n//10 #까먹기전에 n을 갱신하자(1의자리수 버리기)
        if d == 3 or d==6 or d==9:
            print('-',end=" ")
            is369=True
    #반복 종료후에 만약에 369가 아니면?
    if not is369:
        print(i,end=" ")
    else:
        print(" ",end=" ")





