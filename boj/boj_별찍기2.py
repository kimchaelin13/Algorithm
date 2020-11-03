import sys
sys.stdin = open("input.txt", "r")
'''
    *
**
'''

N=int(input())
for i in range(1,N+1):
    print(' '*(N-i),end="")
    print('*'*i)


stars='*****'

#stars를 읽으면서 처음에 1~4까지 삭제하고, 그다음에는 1~3까지 삭제하고,
#그다음에는 1~2, 그다음에는 1 그리고 삭제안함.


n=4
for i in range(len(stars)):
    first=[0:n]
