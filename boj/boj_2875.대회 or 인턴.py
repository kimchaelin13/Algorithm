import sys
sys.stdin=open('input.txt','r')

'''
6 3 2

#1. 인턴인원 제외하고
    남자 여자 주어졌을때 최대 팀수를 구한다.(total)

#2. 팀을 구성하고 남은 인원이 있다면, (남은 인원-K) 하고, 또 그래도 남는 K가 있다면, 하나씩 팀을 해체하고, 마지막 남은 팀을 리턴한다
'''

N,M,K=map(int,input().split())
total=0

#1.
while True:
    for i in range(0,N,2):
        for j in range(0,M):
            if i<N and i+1 < N and j<N:
                total+=1
        print(total)
        #sys.exit()
        break
    break

#팀을 구성하고 남은 인원이 있다면,
if (N+M)-(total*3) != 0:
    K=(N+M)-(total*3)-K
    if K!=0:
        #false
        total-=1
        K-=1
#팀을 구성했는데 여자남자 모두 다썼다면?
else:




