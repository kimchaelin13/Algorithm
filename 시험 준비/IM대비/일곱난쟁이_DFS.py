import sys
sys.stdin = open('input.txt','r')

def dfs(L,sum):
    if L==9:
        if sum==100:
            return
    else:
        dfs(L+1,sum+h[L])
        dfs(L+1,sum)

if __name__=='__main__':
    h=[]
    for _ in range(9):
        h.append(int(input()))
    ##
    res=[]
    dfs(0,0)
    print(res)
