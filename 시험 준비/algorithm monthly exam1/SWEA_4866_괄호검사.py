import sys
sys.stdin = open("input.txt", "r")




for tc in range(1,int(input())+1):
    sentence=input()
    stack=[]
    result=1
    for i in sentence:
        if i in '({':
            stack.append(i)

        elif i in ')}':
            if len(stack)==0: #1
                result=0
                break
            else:
                tmp=stack.pop(-1) #2

            if i==')' and tmp=='(':
                continue
            elif i=='}' and tmp=='{':
                continue
    if len(stack)!=0:#3
        result=0 #4
    print('#{} {}'.format(tc,result))