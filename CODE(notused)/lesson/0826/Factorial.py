def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(3))
#재귀의 기본은
#종료조건(basis)과 반복조건으로 이뤄져있음
#종료조건이 없게 되면? 스택에 계속 쌓이게 되고 메모리가 버틸 수 없기 때문에 stackoverflow가 됨
#그래서 그런걸 막기 위해서 보통은 위와 같이 종료조건, 반복조건을 주게 됨.
