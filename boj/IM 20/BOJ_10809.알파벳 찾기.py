import sys
sys.stdin=open('input.txt','r')

# S=list(input().upper())
# arr=[-1]*26
# ch=[0]*26
# for i in range(len(S)):
#     if ch[ord(S[i])-65] != True:
#         arr[ord(S[i])-65] = i
#         ch[ord(S[i])-65] = True
# print(*arr)
#


S=input()
alpha='abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(S.find(i),end=" ")
