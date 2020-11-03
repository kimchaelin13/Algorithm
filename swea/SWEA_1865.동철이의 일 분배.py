import sys
sys.stdin=open('input.txt','r')

'''
100
4
71 51 30 1
29 63 32 93
84 94 33 21
56 40 80 31
3
13 0 50
12 70 90
25 60 100
 
잘못생각했다 ㅅㅂ 
#1.1번일을 1번째 사람이 선택했을때 
    2번일은 4번째 사람(0.93)이 선택하는게 최대
    3번일은 2번째 사람(0.94)이 하는게 최대
    4번일은 남은 3번 사람이 하는게 최대

#2. 이렇게 1번 사람이 1번일을 할때, 2번일을 할때, 3번일을 할때가 정해지면 나머지가 자동으로 구해짐
#3. 각각의 값을 res에 담고 최대를 구한다.

#내가 만들 프로그램은 0,0이 넘어가면 0,0을 선택했을때 나올 수 있는 최대값을 계산해주는 프로그램이다
'''

# def max_percentage(v,total):
#     global res
#     if total<=res:
#         return
#     if v==N:
#         if total>res:
#             res=total
#     else:
#         for i in range(N):
#             if check[i]==0:
#                 check[i]=1
#                 max_percentage(v+1,total*ability[i][v])
#                 check[i]=0
# for tc in range(1,int(input())+1):
#     N=int(input())
#     ability=[list(map(lambda x:int(x)/100, input().split())) for _ in range(N)]
#     #print(ability)
#     check=[0]*N
#     res=-9876543321
#     max_percentage(0,1)
#     print('#{} {:.6f}'.format(tc, res * 100))



def max_per(L,total):
    global res
    if total <= res:
        return
    if L==N:
        if total>res:
            res=total
    else:
        for i in range(N):
            if check[i]==0:
                check[i]=1
                max_per(L+1,total*ability[i][L]/100)
                check[i]=0

for tc in range(1,int(input())+1):
    N=int(input())
    ability=[list(map(int,input().split())) for _ in range(N)]
    check=[0]*N
    res=-987654321
    max_per(0,1)
    print('#{} {:.6f}'.format(tc,res*100))