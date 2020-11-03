import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    b=int(input())
    a = list(map(int,input()))
    MAX=0
    result=0

    for i in range(len(a)):
        cnt=0
        cnt=a.count(a[i])

        if cnt>MAX:
            MAX=cnt
            result=a[i]

            if MAX==1:
                result=max(a)

    print('#{} {} {}'.format(tc,result,MAX))






