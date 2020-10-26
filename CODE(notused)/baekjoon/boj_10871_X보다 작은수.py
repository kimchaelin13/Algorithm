import sys
sys.stdin = open("input.txt", "r")
#
# n,x=map(int,input().split())
# arr=list(map(int,input().split()))
# for i in arr:
#     if x > i:
#         print(i,end=" ")

#다른
# for i in range(1,int(input())+1):
#     n,m=map(int,input().split())
#     sum=n+m
#     print('Case #{}: {} + {} = {}'.format(i,n,m,sum))

#기찍 N
# for i in range(1,int(input())+1)[::-1]:
#     print(i)

for i in range(int(input())):
    n,m=map(int,input().split())
    print(n+m)