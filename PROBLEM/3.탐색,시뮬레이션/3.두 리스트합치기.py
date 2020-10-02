import sys
sys.stdin=open('input.txt')


n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
p1=p2=0 #포인터변수
c=[]
while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<n:
    c = c+a[p1:]
else:
    c = c+b[p2:]
print(*c)







# n1=int(input())
# a=list(map(int,input().split()))
# n2=int(input())
# b=list(map(int,input().split()))
# res=[]
#
# for i in a:
#     res.append(i)
# for j in b:
#     res.append(j)
#
# print(*sorted(res))
