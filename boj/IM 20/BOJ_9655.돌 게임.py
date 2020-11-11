import sys
sys.stdin=open('input.txt','r')

N=int(input())
#홀수면 상근이가 이기고, 창영이가 이기면
if N%2:
    print('SK')
else:
    print('CY')
