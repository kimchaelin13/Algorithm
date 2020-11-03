import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N=int(input())
    raw_num=list(map(int,input().split()))
    sorted_num=sorted(raw_num)

    result=[]

    while len(result) < 10:
        result.append(sorted_num[-1])
        result.append(sorted_num[0])
        sorted_num=sorted_num[1:len(sorted_num)-1]
    result=' '.join(map(str,result))
    print('#{} {}'.format(tc,result))