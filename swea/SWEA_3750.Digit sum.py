import sys
sys.stdin=open('input.txt','r')
'''
588432

예를 들어 n = 588432라면, f(n) = 5 + 8 + 8 + 4 + 3 + 2 = 30인 것이다.

어떤 자연수 n이 주어질 때, n이 한 자리수가 될 때까지 n에 f(n)을 대입하는 것을 반복하면, 최종적으로 n이 어떤 값이 되는지 구하는 프로그램을 작성하라.

재귀로 짜면 편할거같다
종료조건은 len()==1이 될떄까지
'''

# def plus_digit(n):
#     global res
#     if len(str(n))==1:
#         return n
#     else:
#         res=0
#         for i in n:
#             res+=int(i)
#         plus_digit(str(res))
#     return res
#
# for tc in range(1,int(input())+1):
#     n=input()
#     print('#{} {}'.format(tc,plus_digit(n)))
