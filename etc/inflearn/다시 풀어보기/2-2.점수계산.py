import sys
sys.stdin=open('input.txt','r')

'''
1 0 1 1 1 0 0 1 1 0

1을 만나면 total에 +1을 함
0을 만나면 
'''


N=int(input())
score=list(map(int,input().split()))
total=0
tmp=0
for i in range(N):
    if score[i]==1:
        tmp+=1
    else:
        tmp=0
    total+=tmp
print(total)