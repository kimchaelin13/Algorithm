import sys
sys.stdin = open("input.txt", "r")

# 사칙연산 +, -, *, / 순서로
# 연산한
# 결과를
# 출력한다.

n,m = map(int,input().split())

result = n+m
print(result)