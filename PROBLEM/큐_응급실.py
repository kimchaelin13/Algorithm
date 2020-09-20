import sys
from collections import deque

'''
5 2
60 50 70 80 90
'''

n,m=map(int,input().split())
Q=[(pos, val) for pos,val in enumerate(list(map(int,input().split())))]

#[60,50,70]을 받고, 그걸 enumerate로 접근해서 pos,val을 접근한다면
#(0,60),(1,50),(2,70) 이런식으로 튜플로 받아진다. pos를 하는 이유는 n번째를 알기 위해서!
#이걸 queue 자료구조로 만들거다

Q=deque(Q)
cnt=0 #몇번째인지 물어보는거니까

while True:#n번째 사람이 진료를 받는 순간 출력하고 브레이크해야지
    cur=Q.popleft()
    #이제 대기목록중에 위험도가 cur보다 높으면 진료받지 못하고 뒤로 append되게됨 이걸 어떻게 처리할까?
    #any라는 함수가 있다.
    #cur=(0,60), 이거의 cur[1]은 위험도에 해당함
    #Q에있는 자료를 도는데,x는 튜플값,
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else: #이말은 한개도 참이 아닌것임.any함수.이사람의 위험도가 제일 높다는뜻.진료받자
        cnt+=1
        if cur[0] == m:#m번째 사람이 몇번만에 진료받는지 찾는거니까
            print(cnt)
            break