import sys
sys.stdin=open('input.txt','r')

P=input()
ans = 10
for i in range(1,len(P)):
    if P[i-1] == P[i]:
        ans+=5
    else:
        ans+=10
print(ans)