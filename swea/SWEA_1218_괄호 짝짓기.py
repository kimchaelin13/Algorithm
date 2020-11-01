import sys
sys.stdin = open("input1.txt", "r")

for tc in range(1,int(input())):
    bracket = input()
    stack=[]
    result = 1
    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '[' or bracket[i] == '{' or bracket[i] == '<':
            stack.append(bracket[i])
        elif bracket[i] == ')' or bracket[i] == ']' or bracket[i] == '}' or bracket[i] == '>':
            if len(stack)==0:
                result=0
            else:
                tmp = stack.pop(-1)

            if bracket[i] == ')' and tmp== '(':
                continue
            elif bracket[i] == ']' and tmp== '[':
                continue
            elif bracket[i] == '}' and tmp== '{':
                continue
            elif bracket[i] == '>' and tmp== '<':
                continue
            else:
                result=0

    if len(stack) > 0:
        result=0
    print('#{} {}'.format(tc, result))



# def check(b):
#     stack=[]
#     for i in range(leng):
#         x = b[i]
#         if x in '{(<[':
#             stack.append(x)
#         elif x in '})>]':
#             if len(stack) == 0:
#                 return 0
#             tmp=stack.pop(-1)
#
#             if tmp == '{' and x =='}':
#                 continue
#             elif tmp == '(' and x==')':
#                 continue
#             elif tmp == '[' and x==']':
#                 continue
#             elif tmp == '<' and x=='>':
#                 continue
#             return 0
#     if len(stack) >0:
#         return 0
#     return 1
#
# for tc in range(1,11):
#     leng=int(input())
#     bracket=input()
#     result=check(bracket)
#     print('#{} {}'.format(tc,result))