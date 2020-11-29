import sys
sys.stdin=open('input.txt','r')

'''
#1. 두 문자열의 길이가 같으면 바로 비교
#2. 다르면 길이의 최소공배수를 구해서 두 문자열 모두 최소공배수만큼 문자열을 반복해서 늘리고
#3. 두 문자열을 비교
'''
# def check(S,T):
#     MAX=0
#     MIN=0
#     r_S = S
#     r_T = T
#     global res
#     #최대공약수 구하기
#     for i in range(1,min(n_S,n_T)+1):
#         if n_S%i==0 and n_T%i==0:
#             if i>MAX:
#                 MAX=i
#     #최소공배수 구하기
#     MIN=(MAX*(n_S//MAX)*(n_T)//MAX)
#     if n_S < MIN:
#         while True:
#             r_S+=S
#             if len(r_S) == MIN:
#                 break
#
#     if n_T < MIN:
#         while True:
#             r_T+=T
#             if len(r_T) == MIN:
#                 break
#     if r_T!=r_S:
#         res=0
#         return
# if __name__ == '__main__':
#     S=input()
#     T=input()
#     n_S,n_T=len(S),len(T)
#     res=1
#     if n_S==n_T:
#         if S!=T:
#             res=0
#     else:
#         check(S,T)
#     print(res)
#
#
#

a,b= input(), input()
print(int(a*len(b)==b*len(a)))