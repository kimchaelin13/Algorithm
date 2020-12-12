import sys
sys.stdin=open('input.txt','r')


arr = list(input() for _ in range(5))
st=0
for t in arr:
    if len(t) > st:
        st=len(t)


res = []
for i in arr:
    if len(i)==st:
        res.append(list(i))
    else:
        plus=st-len(i)
        new = i + ' '*plus
        res.append(list(new))
ans=''
for j in range(st):
    for i in range(5):
        ans += res[i][j]
print(ans.replace(" ",""))