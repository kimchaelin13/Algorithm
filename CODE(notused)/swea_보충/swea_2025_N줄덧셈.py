import sys
sys.stdin = open("input.txt", "r")

sum=0
for i in range(int(input())+1):
    sum+=i
print(sum)