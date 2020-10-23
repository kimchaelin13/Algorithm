import sys
sys.stdin=open('input.txt','r')
'''

'''
def DFS(L,sum):
    global res
    if L>N+1:
        return
    if L==N+1:
        if sum>res:
            res=sum
    else:
        DFS(L+timeline[L][0], sum+timeline[L][1])
        DFS(L+1,sum)


if __name__ == '__main__':
    N=int(input())
    timeline=[]
    for i in range(1,N+1):
        t,w=map(int,input().split())
        timeline.append((t,w))
    timeline.insert(0,0)
    #print(timeline)
    res=0
    DFS(1,0)
    print(res)


