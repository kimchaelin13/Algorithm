import sys
sys.stdin = open("input.txt", "r")

txt=input()
up = ''
for i in txt:
    up += i.upper()
print(up)