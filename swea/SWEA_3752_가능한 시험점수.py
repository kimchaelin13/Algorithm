import sys
sys.stdin = open("input.txt", "r")
import time


def DFS(L,sum):
    if sum in result:
        return
    if L>N:
        return
    if sum>total:
        return
    if L==N:
        result.add(sum)
    else:
        DFS(L+1,sum+points[L])
        DFS(L+1,sum)


for tc in range(1,int(input())+1):
    N=int(input())
    points=list(map(int,input().split()))
    result=set()
    total=sum(points)
    DFS(0,0)
    print('#{} {}'.format(tc,len(result)))