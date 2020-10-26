N = int(input())

#내가 구하고 싶은 N까지의 메모를 선언
memo = [-1]*(N+1)

#초기 2개의 값은 미리 초기화
memo[0] = 0
memo[1] = 1

def fibo(N):
    #-1이라는 말은 아직 값이 구해지지 않음
    if memo[N] == -1:
        memo[N] = fibo(N-1)+fibo(N-2)

    #구한값을 리턴 위에 걸리지 않으면 바로 리턴
    return memo[N]
print(fibo(5))
