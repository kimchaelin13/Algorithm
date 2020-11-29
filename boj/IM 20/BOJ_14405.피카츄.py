import sys
sys.stdin=open('input.txt','r')

import sys
input = sys.stdin.readline

s = input().rstrip()

p = s.count('pi')
k = s.count('ka')
c = s.count('chu')

if 2*p+2*k+3*c !=len(s):
    print('NO')
else:
    print('YES')
# S=input()
# N=len(S)
# a=N-1
# flag=0
# if N==1:
#     flag=1
# else:
#     while True:
#         if a<0:
#             break
#         if S[a]=='i':
#             if S[a-1]=='p':
#                 a-=2
#             else:
#                 flag=1
#                 break
#         elif S[a]=='a':
#             if S[a-1]=='k':
#                 a-=2
#             else:
#                 flag=1
#                 break
#         elif S[a]=='u':
#             if S[a-1]=='h' and S[a-2]=='c':
#                 a-=3
#             else:
#                 flag=1
#                 break
#         else:
#             flag=1
#             break
#
# if flag:
#     print('NO')
# else:
#     print('YES')