import sys
sys.stdin = open("input.txt", "r")

nums=[]
for _ in range(9):
    nums.append(int(input()))
MAX=max(nums)
print(MAX,nums.index(MAX)+1,sep='\n')