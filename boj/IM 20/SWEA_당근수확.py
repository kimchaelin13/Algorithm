import sys
sys.stdin=open('input.txt','r')

'''
3
5
10 8 7 4 9
10
9 4 1 6 9 10 0 5 8 2
10
3 1 6 8 0 9 7 9 9 7

#1. 전체 당근 개수 // 2 => 이개수가 되야 이상적임(1번예시에서는 19)
#2. 1번사람이 10까지 함. 차이는? 19-10 = 9 (현재 min 값은 9다)
    1번 사람이 한칸 더가서 18까지함. 차이는? 19-18=1 (현재 min값은 1이다)
    1번 사람이 한칸 더 가서 25까지 함. 차이는? 19-25=절댓값으로 계산해서 6임. 더 커짐 -> 이렇게 되면, 그 전 인덱스까지고,저장된 min 값 출력
    
'''
for tc in range(1,int(input())+1):
    N=int(input())
    farm = list(map(int,input().split()))
    aver=sum(farm)//2
    MIN=9876543321
    wordload_1=0
    temp_1=0
    w_1=0
    for i in range(N):
        wordload_1 += farm[i]
        temp_1 = abs(aver - wordload_1)
        if MIN > temp_1:
            MIN=temp_1
            w_1=i
    res_11=sum(farm[:w_1+1])
    res=abs((sum(farm)-res_11) - res_11)
    #print(res)
    #w_1은 1이 한 인덱스
    print('#{} {} {}'.format(tc,w_1+1,res))



