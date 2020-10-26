import sys
sys.stdin = open("input.txt", "r")

s = []
for i in range(5):
    s.append(int(input()))
for j in range(len(s)):
    if s[j] < 40:
        s[j]=40
print(round(sum(s)/len(s)))