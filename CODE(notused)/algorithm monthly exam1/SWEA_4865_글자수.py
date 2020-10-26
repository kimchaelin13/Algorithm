import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    str1=input()
    str2=input()
    A=len(str1)
    B=len(str2)
    cnt=0
    for i in str1:
        sub_cnt=0
        for j in str2:
            if i==j:
                sub_cnt+=1
        if sub_cnt>cnt:
            cnt=sub_cnt
    print('#{} {}'.format(tc,cnt))



