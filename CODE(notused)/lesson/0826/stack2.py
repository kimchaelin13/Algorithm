#자료구조필요하니까
stack =[]

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print("Stack is empty") #비어있는지 고려해야함!
        return
    else:
        return stack.pop()

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())