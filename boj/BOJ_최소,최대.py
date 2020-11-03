import sys
sys.stdin = open("input.txt", "r")

n=input()
nums=list(map(int,input().split()))
print(min(nums),max(nums))


