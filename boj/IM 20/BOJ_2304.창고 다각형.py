import sys
sys.stdin=open('input.txt','r')

'''
1.앞에를 기준으로 정렬함(위치기준)
2.두번째 높은 기둥을 찾아서 적절한 연산을 한다.
3.가장높은 기둥~ 두번째 높은 기둥 사이에 있는 x는 가지 않아야 하기 때문에 체크해야함.
4.세번째 기둥 찾고, 적절한 연산을하고,,그러다가
5.만약에 첫번쨰 x축~마지막x축까지 모두 방문했다고 나오면 그만!
'''



#1.입력 받기
N=int(input())

info=[0]*21
for _ in range(N):
    pos,height=map(int,input().split())
    info[pos]=height

#2.가장 높은 기둥의 인덱스가 어디있는지 찾는다
H,H_POS=0,0
for h in info:
    if h>H:
        H=h
        H_POS=info.index(H)

#print(info)
#3.오른쪽
temp_h=0
area=0
for i in range(0,H_POS):
    if info[i]>temp_h:
        temp_h=info[i]
    area += temp_h

#4.왼쪽
temp_h=0
for i in range(20,H_POS,-1):
    if info[i]>temp_h:
        temp_h=info[i]
    area+= temp_h

#제일 큰 기둥
print(area+H)