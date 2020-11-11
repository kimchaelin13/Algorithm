import sys
sys.stdin=open('input.txt','r')




arr=[[0]*100 for _ in range(100)]
for tc in range(int(input())):
    x,y=map(int,input().split())
    xx,yy=x+10,y+10

    for r in range(x,xx):
        for c in range(y,yy):
            arr[r][c]=1
ans=0
for row in arr:
    ans += sum(row)
# for r in range(100):
#     for c in range(100):
#         if arr[r][c]==1:
#             ans+=1
print(ans)