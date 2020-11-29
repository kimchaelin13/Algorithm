import sys
sys.stdin=open('input.txt','r')

N=int(input())
for _ in range(N):
    S=input()
    N=len(S)
    stack=[]
    flag=0
    for i in range(N):
        if S[i]=='(':
            stack.append(S[i])
        else:
            if not stack:
                flag=1
            else:
                stack.pop()
    if flag==1 or stack:
        print('NO')
    else:
        print('YES')

# def check(S):
#     stack=[]
#     for i in S:
#         if i=='(':
#             stack.append(i)
#         else:
#             if not stack:
#                 print('NO')
#                 return
#             else:
#                 stack.pop()
#     if not stack:
#         print('YES')
#         return
#     else:
#         print('NO')
#         return
#
# for _ in range(int(input())):
#     S=input()
#     check(S)
