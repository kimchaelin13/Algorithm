import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    chars=input()
    stack=[]
    for i in range(len(chars)):
        stack.append(chars[i])
        if len(stack)>1:
            if stack[-1]==stack[-2]:
                del stack[-2:]
    print('#{} {}'.format(tc,len(stack)))
