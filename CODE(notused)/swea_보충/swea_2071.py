
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    nums = list(map(int,input().split()))
    for i in nums:
        sum += i
        avg = round(sum/len(nums))

    print(f'#{test_case} {avg}')


