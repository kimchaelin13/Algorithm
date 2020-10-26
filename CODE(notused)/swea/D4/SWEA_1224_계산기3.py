'''
formula의 길이만큼 돌면서
여는 괄호를 만나면 무조건 스택에 push한다
닫는 괄호를 만나면 stack에서 여는 괄호가 나올때까지 pop함
여는괄호의 우선순위는 제일 작다
괄호는 출력하지 않는다.

1. 피연산자는 그냥 출력
2. 연산자는 스택이 비어있으면, 스택에 push한다.
3. 비어 있지 않는다면? 스택에 있는 연산자와 비교해서 우선순위가 같거나 크다면 스택에 있는 연산자 pop하고 출력, 현재 연산자는 스택에 push한다.
#                                          현재 연산자의 우선쉬위가 더 크면 현재 연산자를 push!@!


(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)
'''



import sys
sys.stdin = open("input1.txt", "r")

priority={"*":2, '/':2,'+':1,'-':1,'(':0}

###############중위 표기식 -> 후위표기식##################
for tc in range(1,11):
    input()
    line=input()
    ans=''

    stack=[]

    for i in range(len(line)):
        #여는 괄호는 우선순위가 제일 높으므로 무조건 삽입
        if line[i] == '(' or line[i] == ')':
            if line[i] == '(':
                stack.append(line[i])

            else:
                #여는괄호가 나올때까지 무조건 pop
                while stack[-1] != '(':
                    ans += stack.pop()
                #야는 괄호하나 버리기
                stack.pop()

        elif line[i].isdigit():
            ans+=line[i]

        #연산자일때
        else:
            if len(stack) == 0:
                stack.append(line[i])
            else:
                #연산자 우선순위 비교해서
                #스택에 탑에 있는 연산자가 현재 토큰의 우선순위보다 높거나 같다면
                while priority[stack[-1]] >= priority[line[i]]:
                    ans+=stack.pop()
                    if len(stack)==0:
                        break
                stack.append(line[i])
    #남아있는 스택 비우기
    while len(stack)>0:
        ans+=stack.pop()



##########꺼내서 계산하는 과정#################

    for i in ans:
        #숫자면 스택에 쌓기, 스택을 비워놨기 때문에 가능함!
        if i.isdigit():
            stack.append(int(i))

        #연산자이면 꺼내서 연산후 다시 삽입
        else:
            B=stack.pop()
            A=stack.pop()
            if i == '+':
                stack.append(A+B)
            elif i=='-':
                stack.append(A-B)
            elif i=='*':
                stack.append(A*B)
            elif i=='/':
                stack.append(A/B)
    print("#{} {}".format(tc, stack.pop()))






