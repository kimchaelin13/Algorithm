import sys
sys.stdin=open('input.txt','r')

'''
N=3

i=0 별 9개 : 4(n-1)+1
i=1 L 1개 공백 7개 R 0개
i=2 L 1개 별 7개 R 0개
i=3 L 2개 공백3개 R 1개
i=4 L 2개 별3개 R 2개
i=5 L 5개

i=6 L 5개
i=7 L 2개 공백1 R 2개
i=8 L 1개 별5개 R 1개
i=9 L 1개 공백5개 R 1개
i=10 별 9개

middle=전체길이인 11//2

0~(middle-1) 까지 -> 규칙1

middle, middle+1 -> middle의 인덱스숫자만큼 L*

middle+2 ~ 끝까지 -> 규칙 2 (middle+2에는 위에서 L_CNT=R_CNT로 하고, -1씩하고 
    그 다음부터는 홀수일때 -1씩함
'''

N=int(input())
length=4*N-1
L_star='* '
R_star=' *'
T_CNT=4*(N-1)+1
L_cnt,R_cnt,EMPTY_CNT=1,0,T_CNT-2
middle=length//2

if N==1:
    print('*'*1)

else:
    for i in range(length):

        #level1
        if i<middle:
            if i==0:
                print('*'*T_CNT)
            if i==1:
                print('*')
            elif i%2:
                print(L_star*L_cnt + ' '*EMPTY_CNT + R_star*R_cnt)
            elif i!=0 and i%2==0:
                print(L_star * L_cnt + '*'*EMPTY_CNT + R_star*R_cnt)
                L_cnt+=1
                R_cnt+=1
                EMPTY_CNT = T_CNT - 2*(L_cnt+R_cnt)
        #
        # level2
        elif i==middle:
            print(L_star * middle)

        elif i==middle+1:
            print(L_star * middle)

            L_cnt-=1
            R_cnt = L_cnt
            EMPTY_CNT = 1

        #level3
        elif middle+1<i<length-1:
            if i%2:
                print(L_star * L_cnt + ' '*EMPTY_CNT + R_star * R_cnt)
                L_cnt-=1
                R_cnt-=1
                EMPTY_CNT = T_CNT - 2*(L_cnt+R_cnt)
            elif i%2==0:
                print(L_star*L_cnt + '*'*EMPTY_CNT + R_star*R_cnt)
        else:
            print('*'*T_CNT)


