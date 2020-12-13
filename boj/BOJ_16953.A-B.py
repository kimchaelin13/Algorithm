import sys
sys.stdin=open('input.txt','r')

def dfs(A,cnt):
    global MIN,flag
    if cnt>MIN:
        return
    if int(A)>int(B):
        return
    if int(A)==int(B):
        if MIN>cnt:
            MIN=cnt
            flag=1

    dfs(int(A)*2,cnt+1)
    dfs(str(A)+'1',cnt+1)

A,B=input().split()
flag=0
MIN=987654321
dfs(A,0)

if flag:
    print(MIN+1)
else:
    print('-1')