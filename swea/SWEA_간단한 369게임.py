import sys
sys.stdin=open('input.txt','r')

'''


'''




N=int(input())

for n in range(1,N+1):
    strN= str(n)
    cnt = 0
    for n in strN:
        if ('3' in n) or ('6' in n) or ('9' in n):
            cnt += 1
    if cnt > 1:
        strN = '--'
    elif cnt == 1:
        strN = '-'
    print(strN,end = ' ')