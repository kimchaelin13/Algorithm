import sys
sys.stdin=open('input.txt','r')

'''
3
5
20 23
17 20
23 24
4 14
8 18

#1.입력받고
#2.끝나는 시간을 기준이 앞선것을 기준으로 정렬한다.
#3.처음에 나온건 무조건 선택함. 끝나는 시간이 14다. 그러면 그다음 시작시간은 14 이후여야 함,
'''

for tc in range(1,int(input())+1):
    N=int(input())
    timeline=[]
    for _ in range(N):
        s,e=map(int,input().split())
        timeline.append((s,e))

    timeline.sort(key=lambda x:(x[1],x[0]))
    #print(timeline)

    tmp=0
    cnt=0
    for s,e in timeline:
        if s>=tmp:
            tmp=e
            cnt+=1
    print('#{} {}'.format(tc,cnt))
