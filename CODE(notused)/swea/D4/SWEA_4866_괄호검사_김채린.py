import sys
sys.stdin = open("input1.txt", "r")

def check(b):
    stack=[]
    for i in range(len(b)):
        x = b[i]
        if x in '{(':
            stack.append(x)
        elif x in '})':
            if len(stack) == 0:
                return 0
            tmp=stack.pop(-1)

            if tmp == '{' and x =='}':
                continue
            elif tmp == '(' and x==')':
                continue
            return 0
    if len(stack) >0:
        return 0
    return 1

for tc in range(1,int(input())+1):
    bracket=input()
    result=check(bracket)
    print('#{} {}'.format(tc,result))