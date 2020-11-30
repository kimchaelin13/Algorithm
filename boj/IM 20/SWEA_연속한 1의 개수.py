'''
1이 나오면 연속된 1의 cnt를 센다
0이 나오면 MAX(초기설정0) 과 비교해서 만약 CNT가 더 크면, MAX를 CNT로 초기화하고,CNT는 0으로 초기회
'''
import sys
sys.stdin=open('input.txt','r')
for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,list(input()))) + [0]
    MAX=0
    CNT=0
    for i in range(N+1):
        if nums[i]==1:
            CNT+=1
        else:
            if CNT>MAX:
                MAX=CNT
                CNT=0
    print('#{} {}'.format(tc,MAX))