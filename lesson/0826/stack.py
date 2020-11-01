# C style

stack=[0]*100 #고정
top = -1 #top을 -1로 초기화함.왜 1로 초기화하지??

def push(item):
    global top
    #이게 top이 밖에 있어서 안에서 값을 변경해도 변경이 안됨 그래서 globla어쩌고를 하는거임
    if top > 100-1: #99가 되면 못넣는다 왜? 인덱스는 0~99까지 있으니까!!
        return

    else:
        top += 1
        stack[top] = item


def pop(): #isEmpty인지 항상 체크해야함
    global top(값형, read만 되기 때문에 꼭
               )
    if top == -1:
        print("Stack is Empty")
        return

    else:
        result = stack[top]
        top -=1
        return result


stack = [0]*100
top = -1

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())


