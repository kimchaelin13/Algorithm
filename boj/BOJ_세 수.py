import sys
sys.stdin = open("input.txt", "r")

a=list(map(int,input().split()))
a.sort(reverse=True)
print(a[1])