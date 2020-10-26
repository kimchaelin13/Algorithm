import sys
sys.stdin = open("input.txt", "r")

for i in range(int(input())+1):
    print(2**i,end=" ")