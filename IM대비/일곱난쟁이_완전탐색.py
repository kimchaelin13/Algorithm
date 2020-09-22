import sys
sys.stdin = open('input.txt','r')
'''
일곱명의 키가 100이여야 함.
그러면 9명합 - 특정 2명 = 100(나머지7명)
'''
h=sorted([int(input()) for _ in range(9)])
N=9
res=[]
for i in range(N):
    for j in range(i,N):
        if sum(h)-h[i]-h[j]==100:
            for k in range(N):
                if k!=i and k!=j:
                    print(h[k])
            sys.exit()



#
# #random함수 이용
# import random
# h=[int(input()) for i in range(9)]
# l=[]
# while True:
#     l=random.sample(h,7)
#     s= sum(l)
#     if s==100:
#         break
# for i in range(7):
#     #근데 이거 뭐지? 아래꺼처럼 어떻게 하는건지 잘 모르겠당
#     print(sorted(l)[i])
#
import sys
sys.stdin=open('input.txt','r')

import itertools
for com in itertools.combinations([int(input()) for _ in range(9)],7):
    if sum(com)==100:
        print(*sorted(com),sep='\n')
