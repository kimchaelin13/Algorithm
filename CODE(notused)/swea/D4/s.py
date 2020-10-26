for tc in range(1,11):
    leng = int(input())
    bracket = input()
    stack=[]

for i in range(leng):
    if bracket[i] == '(' or bracket[i] == '[' or bracket[i] == '{' or bracket[i] == '<':
        stack.append(bracket[i])
    elif bracket[i] == ')' or bracket[i] == ']' or bracket[i] == '}' or bracket[i] == '>':
        if len(stack)==0:
            result = 0
            break
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
        result=0 #1

if len(stack) > 0:
    result=0
else: result=1

print('#{} {}'.format(tc, result))