import sys
sys.stdin=open('input.txt','r')

S=input()
sol = {}
temp=97
while temp <=122:
    for i in S:
        sol[chr(temp)] = i
        temp+=1
code=input()
res=''
for i in code:
    if i==' ':
        res += ' '
    else:
        res += sol.get(i)
print(res.capitalize())