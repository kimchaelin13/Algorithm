import sys
sys.stdin=open('input.txt','r')

'''
#1.10이 들어오면 (1,11)까지 돌면서 =
#2.이걸 문자로 바꾼다
#3.그리고 3,6,9가 들어있으면 cnt를 세주고
#4.그 '-'cnt 만큼 출력하게 한다
'''


N=int(input())
flag=1
for i in range(1,N+1):
    cnt=0
    a=str(i)
    for j in a:
        if ('3' in a) or ('6' in a) or ('9' in a):
            cnt+=1
    if cnt>0:
        print('-'*cnt,end=" ")
    else:
        print(a,end=" ")
