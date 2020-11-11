import sys
sys.stdin=open('input.txt','r')

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
res = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            res += dial.index(j)+3
print(res)