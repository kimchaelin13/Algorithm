import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    str1=input()
    str2=input()
    A=len(str1)
    B=len(str2)

    result=0
    for i in range(B-A+1):
        for j in range(A):
            if str2[i:i+A] == str1:
                result=1
                break
    print('#{} {}'.format(tc,result))
