import sys
sys.stdin=open('input.txt','r')

'''
n은 100까지임 그러면 100배열을 만들고
체를 만들고

=> [1,3,5,7] 배열 만들고
=> for문 2개 돌면서
=> for i in range(2,101):
    for j in list:
        if check[j]==0:
            cnt+=1
'''

ch=[1,1]+[0]*101
n=int(input())

for i in range(2,101):
    for j in range(i+i,101,i):
        ch[j]=1

nums=list(map(int,input().split()))
cnt=0
for j in nums:
    if ch[j]==0:
        cnt+=1
print(cnt)