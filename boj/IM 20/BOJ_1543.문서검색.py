import sys
sys.stdin=open('input.txt','r')


D=input()
S=input()
s=0
cnt=0
e = len(S)
while s<=len(D):
    if D[s:s+e] == S:
        cnt +=1
        s += e
    else:
        s +=1
print(cnt)