import sys
sys.stdin=open('input.txt','r')
'''
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(node):
    visit[node]=True
    if node>V+1:
        return

    else:
        print(node,end=" ")
        if visit[node]==False:
            for i in tree[node]:
                preorder(i)

V=int(input())
tree=[[]*(V+1) for _ in range(V+1)]
nums=list(map(int,input().split()))
for i in range(0,len(nums),2):
    tree[nums[i]].append(nums[i+1])
visit=[False]*(V+1)
#print(visit)
#print(tree)
preorder(1)