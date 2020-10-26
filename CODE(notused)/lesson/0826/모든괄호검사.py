#일단 스택안에 입력값을 넣어두고(리스트)
#만약에 {가 스택안에 있으면 그것과 함께 같이 지우고
#[가 있고. 또 ]가 있으먄?
#근데 나는 이거 포함관계라는게 뭔말인지 잘 모르겠다.


def check(bracket):
    #인자로 넘어온 괄호들을 순회하면서 검사한다
    #여는 괄호라면 무조건 푸쉬
    #닫는 괄호라면 스택의 탑 위치와 비교하여 제 짝이면 pop
    #제 짝이 아니라면 false
    #그리고 모든 검사가 끝까지 순회했을때 스택의 길이가 0이 아니라면 역시 fasle
    stack =[]
    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i]=='[' or bracket[i]=='{':
            stack.append(bracket[i])
        elif bracket[i] == ')' or bracket[i]==']' or bracket[i]=='}':
            if len(stack) == 0: #닫힌경우가 먼저 나온경우!!
                return False
            tmp=stack.pop()

            if bracket[i] == ')' and tmp == '(':
                continue
            elif bracket[i] == '}' and tmp == '{':
                continue
            elif bracket[i] == ']' and tmp == '[':
                continue
            return False

    if len(stack)>0:
        return False
    return True

# for _ in range(int(input())):
#     brcket=input()
#
#     print(check(bracket))

print(check('{()}{[]}'))