import sys
sys.stdin = open('input.txt', 'r')

N=int(input())
for i in range(1,10):
    result=N*i
    print('{} * {} = {}'.format(N,i,result))
