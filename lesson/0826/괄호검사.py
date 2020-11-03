

def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(' : #push 왼쪽괄호 만나면 push
            stack.append(arr[i])
        elif arr[i] == ')' : #pop하고 비교해야함
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if stack: return Fasle #스택이 비어이지않다면 뭔가 잘못된것
    else: return True

stack=[]
arr = '()()((()))'
print(check(arr))