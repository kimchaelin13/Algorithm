import sys
sys.stdin=open('input.txt','r')


''''''
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

'''
N = int(input())
i = 1
while i <= N:
    strI = str(i)
    cnt = 0
    if '3' in strI:
        cnt += strI.count('3')9
    if '6' in strI:
        cnt += strI.count('6')
    if '9' in strI:
        cnt += strI.count('9')
    if cnt:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
    i += 1
'''