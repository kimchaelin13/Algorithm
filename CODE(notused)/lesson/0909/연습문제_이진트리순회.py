'''
swea 1248과 비슷해염
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
#
# def preOrder(index):
#     print(tree[index],end=" ")
#
#     if tree[index*2] !=0:
#         preOrder(index*2)
#
#     if tree[index*2+1] != 0:
#         preOrder(index*2+1)
#
#
# def inOrder(index):
#
#     if tree[index * 2] != 0:
#         preOrder(index * 2)
#     print(tree[index], end=" ")
#     if tree[index * 2 + 1] != 0:
#         preOrder(index * 2 + 1)
#
#
# def postOrder(index):
#
#     if tree[index * 2] != 0:
#         preOrder(index * 2)
#
#     if tree[index * 2 + 1] != 0:
#         preOrder(index * 2 + 1)
#     print(tree[index], end=" ")
# N=int(input())
# info=list(map(int,input().split()))
# tree=[0]*100 #걍 100개라고 설정
#
#
# #두칸씩 자르고 처음칸 부모, 두번째 자식
# for i in range(0,len(info),2):
#     p=info[i]
#     c=info[i+1]
#
#     if p not in tree:
#         idx=-1
#     else:
#         idx=tree.index(p)
#
#     if idx==-1:
#         tree[1]=p
#         tree[2]=c
#     else:
#         if tree[idx*2]==0:
#             tree[idx*2]==c
#         else:
#             tree[idx*2+1]=c
# preOrder(1)
# inOrder(1)
# postOrder(1)
def preorder(node):
    global cnt
    if node != 0:
        print(node,end=" ")
        cnt+=1
        preorder(tree[node][0])
        preorder(tree[node][1])

#정점
V=int(input()) #정점
E=V-1 #간선
tree = [[0]*3 for _ in range(V+1)] #14*3, 열을 먼저준다. 초기화할때
temp=list(map(int,input().split()))
cnt=0
#tree 저장
for i in range(E):
    p,c=temp[i*2],temp[i*2+1]
    if tree[p][0] == 0:
        tree[p][0]=c #left
    else:
        tree[p][1]=c #right
    # 부모
    tree[c][2]=p #parent

# for t in tree:
#     print(*t)

preorder(1)
print(cnt)
