import sys
import random
sys.stdin=open('input.txt','r')

'''
입력=8
8보다 작은 수 중에 소수인 리스트를 생성(2제외) 
그리고 random.sample 써서, l=random2개/


'''

n=int(input())

#소수 리스트 생성
sosu=[]
ch=[0]*(n+1)

for i in range(2,n+1):
    if ch[i]==0:
        sosu.append(i)
        for j in range(i,n+1,i):
            ch[j]=1
print(sosu)

2개를 뽑아서 2개의 합이 n인지 확인
for j in range(len(sosu)):
    for k in range(j,len(sosu)): #여기서도 처음에는 (1,len(sosu)+1)이렇게 했는데,,진짜 이증 for문에서 인덱스에러 매니지 너무 어려워여 ,,,,,,,나올떄마다 1추가하고 1빼고 이런식
        if sosu[j]+sosu[k]==n:
            # print(sosu[j])
            # print(sosu[k])
            print('{} = {} + {}'.format(n,sosu[j],sosu[k]))
            sys.exit()
        else:
            print("Goldbach's conjecture is wrong.")
            sys.exit() 이코드를 넣으면 이상하게 출력됨

'''
구글링해서 결국 찾아봤다...ㅠ
'''
def Goldbach():
    check = [1, 1] + [0] * 1000000

    for i in range(2, 1001): #근데 이건 왜 1000번만 돌지? 아 j가 다 돌아줌
        if check[i] == 0:
            #소수예제코드랑 헷갈렸음
            #여기서는 i+i를 하는게 최종적으로 check배열에 소수면 다 0으로 놔두게할거임
            #그래서 0이면(소수면) 그대로 놔둬야하기때문에! i+i로 뛰어넘어서 그거의 배수를 다 제거(1로 만듦)
            for j in range(i + i, 1000001, i):
                check[j] = 1

    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break

        A = 0
        B = n
        for _ in range(1000000):
            #n을 만들 수 있는지 찾고 n을 만들 수 있다면 f-스트링을 이용한 출력문을 출력하고 break를 통해 빠져나온다.
            #근데 왜 if check[A] ==0 and check[B]==0: 이 코드가 'n을 만들수있는지'에 해당하는지 모르겠다. !!!!
            if check[A] ==0 and check[B]==0:
                print(f"{n} = {A} + {B}")
                break
            A += 1
            B -= 1
        else:
            print("Goldbach's conjecture is wrong.")


Goldbach()