import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    sum=0
    for i in nums:
        if i%2 :
            sum += i
    print(f'#{test_case} {sum}')

