import sys
sys.stdin=open('input.txt','r')

flag=0
for _ in range(int(input())):
    stack=[]
    S=input()
    for i in range(len(S)):
        if len(stack)==0:
            if S[i] == ')': flag=1; break
            else:
                stack.append(S[i])
        else:
            if stack[-1] == '(':
                if S[i]==')':
                    stack.pop()
                else:
                    stack.append(S[i])
            elif stack[-1] == ')':
                if S[i] == '(':
                    stack.pop()
                else:
                    stack.append(S[i])
    if len(stack) or flag==1 :
        print('NO')
    else:
        print('YES')