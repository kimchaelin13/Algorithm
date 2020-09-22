## 1.일곱난쟁이

**import random**

```python
import random
h=[int(input()) for i in range(9)]
l=[]
while True:
    l=random.sample(h,7)
    s= sum(l)
    if s==100:
        break
for i in range(7):
    #근데 이거 뭐지? 아래꺼처럼 어떻게 하는건지 잘 모르겠당
    print(sorted(l)[i])
```



**for문(완전탐색)**

```python
import sys
sys.stdin = open('input.txt','r')

h=sorted([int(input()) for _ in range(9)])
N=9
res=[]
for i in range(N):
    for j in range(i,N):
        if sum(h)-h[i]-h[j]==100:
            for k in range(N):
                if k!=i and k!=j:
                    print(h[k])
            sys.exit()
```



**itertools**

```python
import sys
sys.stdin=open('input.txt','r')

import itertools
for com in itertools.combinations([int(input()) for _ in range(9)],7):
    if sum(com)==100:
        print(*sorted(com),sep='\n')
```



## 2.직사각형 합집합



```python
board=[[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j]=1
            
ans=0
for i in range(101):
    ans+=sum(board[i])
print(ans)
```

색칠하기랑 똑같은데!!!!!!!!!! 이건 좌표기준이 아니라 꼭짓점임 생각해보면 (1,2) (4,4) 사이 좌표에 1을 찍어야함. 6개

![image-20200922230405995](IM대비.assets/image-20200922230405995.png)





## 3. 색종이

2번이랑 개똑같은 문제,,이런거 나오면 좋아서 울것같다 ㅠ 

역시 꼭짓점 값인걸 주의하자! 

```python
import sys
sys.stdin=open('input.txt','r')

'''
왼쪽 아래 좌표인 3,7이 정해지면 오른쪽 위쪽 좌표도 정해진다. -> (3,7) (13,17)
이런식 그러면 보드 100*100을 만들고
3,7을 받고, 범위 설정은 (3,10+3) 하면서 돌아준다 ㅇㅋ
'''

board=[[0]*102 for _ in range(102)]
n=int(input())

for _ in range(n):
    x1,y1=map(int,input().split())

    for i in range(x1,x1+10):
        for j in range(y1,y1+10):
            if board[i][j]==0:
                board[i][j]=1

ans=0
for i in range(102):
    for j in range(102):
        if board[i][j]==1:
            ans+=1
print(ans)

```



## 4. 수 이어가기

```python
N=int(input())
res=-1234
res_list=[]
for i in range(N+1):
    temp=[N,i]
    while True:
        a=temp[-2]-temp[-1]
        temp.append(a)
        if a<0:
            break

        if len(temp)>res:
            res=len(temp)
            res_list=temp[:]

print(res)
print(*res_list)
```

내가 푼 것 70퍼센트 ㅎ 수열을 이해해야 한다. 규칙성! 