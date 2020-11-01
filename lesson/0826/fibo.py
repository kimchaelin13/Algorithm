def fibo(n):
    if n < 2: #멈추는 부분, 기본파트
        return n #0일때는 0, 1일때는 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(8))