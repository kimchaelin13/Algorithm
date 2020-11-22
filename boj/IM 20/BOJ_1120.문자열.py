import sys, copy
sys.stdin=open('input.txt','r')


# def MIN_diff(A,B):
#     # 2개의 길이가 같을때
#     ans = 0
#     if len(A) == len(B):
#         s = 0
#         while s < len(A):
#             if A[s] != B[s]:
#                 ans += 1
#             s += 1
#         return ans
#
#     elif len(A) < len(B):
#         c = 0
#         MIN = 987654321
#         while c <= len(B) - len(A):
#
#             s_A = 0
#             s_B = c
#             ans = 0
#             while s_A < len(A) or s_B < len(A):
#                 if A[s_A] != B[s_B]:
#                     ans += 1
#                 s_A += 1
#                 s_B += 1
#             c += 1
#             if MIN > ans:
#                 MIN = ans
#         return MIN
#
# A,B=input().split()
# print(MIN_diff(A,B))


x, y = input().split()
minimum = 50

for i in range(len(y) - len(x) + 1):
    temp = 0
    for j in range(len(x)):
        if x[j] != y[i + j]:
            temp += 1
    if temp < minimum:
        minimum = temp

print(minimum)