import sys
sys.stdin=open('input.txt','r')


S=input()
misa=''
res=[]
for i in range(len(S)):
    misa=S[i:]
    res.append(misa)
res.sort()
for i in res:
    print(i)