import sys
sys.stdin=open('input.txt','r')

def dfs(L,cnt,total,res):
    global flag

    if flag:
        return
    if total>100:
        return
    if cnt>7:
        return

    if L == 9:
        if cnt==7:
            if total == 100:
                flag=1
                for i in sorted(res):
                    print(i)
        return

    else:
        res.append(h[L])
        #print('append', res, cnt+1)
        dfs(L+1,cnt+1,total+h[L],res)
        res.pop()
        #print('pop',res,cnt)
        dfs(L+1,cnt,total,res)

h=[]
for i in range(9):
    h.append(int(input()))

res=[]
flag=0
#dfs(cnt, total, res)
dfs(0,0,0,res)
