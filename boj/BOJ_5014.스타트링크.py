import sys
sys.stdin=open('input.txt','r')


'''
def dfs(total,cnt):
    global MIN, flag
    if cnt>MIN:
        return
    if total<1 or total>F:
        return
    if total>G:
        return

    if total==G:
        if MIN>cnt:
            MIN=cnt
            flag=1
    else:
        dfs(total+U,cnt+1)
        dfs(total-D,cnt+1)

F,S,G,U,D = map(int,input().split())
MIN=987654321
flag=0
dfs(S,0)

if flag==1:
    print(MIN)
else:
    print('use the stairs')
'''

