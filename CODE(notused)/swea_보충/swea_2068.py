import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int,input().split()))
    max=0
    for num in nums:
        if max < num:
            max = num
    print(f'#{test_case} {max}')

