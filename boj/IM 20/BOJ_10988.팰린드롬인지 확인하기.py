import sys
sys.stdin=open('input.txt','r')

p = input()

ans=0
if p == p[::-1]:
    ans=1
print(ans)
