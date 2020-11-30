import sys
sys.stdin=open('input.txt','r')

'''
#1. 0번째 인덱스에 있는것도 수레에 넣는건지,,?
#2. 0번인덱스는 포함x????
#3.

10 8 7 4 9

거리+=인덱스번호
수레=0

수레+=인덱스의 value
만약 수레용량보다 초과한다면? 거리 += 인덱스번호*2
                        인덱스값 = 수레에 있는 값 % 수레용량
                        수레=0
                        시작인덱스(s)=원래 인덱스
만약 수레용량보다 작다면? s를 이동
                      거리 +=1
                      수레 += 이동한 곳 인덱스의 value


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    # print(arr)
    remain = 0
    dist = 0    #이동거리
    for i in range(N):
        time = (remain + arr[i]) // M   #왕복횟수
        remain = (remain+ arr[i]) % M   #남은 당근수
        dist += ((i+1) * 2 * time)
    if remain >0 :
        dist += (2 * N) #마지막 칸에 남은 당근 회수
    print("#{} {}".format(tc, dist))
'''

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    farm=[0]+list(map(int,input().split()))
    #print(farm)
    load=0
    dist=0
    for i in range(1,N+1):
        load += farm[i]
        if load>=M:
            dist += (i*2) * (load//M)
            load = load%M
    if load>0:
        dist += N*2
    print('#{} {}'.format(tc,dist))

