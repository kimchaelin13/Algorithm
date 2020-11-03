'''

stack(-2)가 앞에 잇어애돼 b*a
숫자면 스택에 넣어버림. 그리고 숫자가 아닌걸 만나면?
제일 끝에 있는걸,  a로 하고 그 안쪽에 있는걸 b로 함

10 2 + 3 4 + * .
'''
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    maze=input().split()
    stack=[]
    flag=0

    for i in range(len(maze)-1):
        #숫자면 스택으로
        if maze[i].isdigit():
            stack.append(maze[i])

        else:
            try:
                A,B = int(stack.pop()),int(stack.pop())

                if maze[i] == '+':
                    result=A+B
                if maze[i] == '*':
                    result = A * B
                if maze[i] == '/':
                    result = B//A
                if maze[i] == '-':
                    result = A - B

                stack.append(result)

            except:
                flag=1234

    if flag==0 and len(stack)==1:
        print('#{} {}'.format(tc,stack[0]))
    elif flag==1234 or len(stack)>1:
        print('#{} error'.format(tc))




