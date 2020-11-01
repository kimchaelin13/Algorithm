import sys
sys.stdin = open("input1.txt", "r")
'''
'''
for tc in range(1,int(input())+1):
    string = input()
    stack = []
    for i in range(len(string)):
        stack.append(string[i])
        #만약에 stack에 들어와있는 가장 윗값 두개가 같다면 두개를 모두 삭제한다.
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                del stack[-2:]
    print('#{} {}'.format(tc,len(stack)))
