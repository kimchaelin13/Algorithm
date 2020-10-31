import sys
sys.stdin=open('input.txt','r')

'''
3
1 2 5
15

#1.[5,2,1]로 정렬하고
#2.
'''

def dfs(L,total):
    global MIN
    if L>MIN:
        return
    if total>change:
        return
    if total==change:
        if L<MIN:
            MIN=L

    else:
        for i in range(N):
            dfs(L+1,total+coins[i])

if __name__ == '__main__':
    N=int(input())
    coins=list(map(int,input().split()))
    change=int(input())
    coins.sort()
    MIN=9876544321
    dfs(0,0)
    print(MIN)