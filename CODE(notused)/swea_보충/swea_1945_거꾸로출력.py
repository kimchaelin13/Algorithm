import sys
sys.stdin = open("input.txt", "r")

for i in range(int(input())+1)[::-1]:
    print(i,end=" ")