import sys
sys.stdin = open("input.txt", "r")
T = int(input())
txt =''
for i in range(T):
    txt += '#'
print(txt)