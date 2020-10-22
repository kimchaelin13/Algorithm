import sys
sys.stdin=open('input.txt','r')

''''
2번으로 했는데 됐고 1번은 틀림 

이 코드는 대체 왜 안되는걸까?,,,,
'''
#pass
n,k=map(int,input().split())

ch=[0]*(n+1)
cnt=0


for i in range(2,n+1):
    for j in range(i,n+1,i):
        if ch[j]==1:
            continue
        else:
            ch[j]=1
            cnt+=1
        if cnt == k:
            print(j)


'''
#pass된 코드
n,k=map(int,input().split())

ch=[0]*(n+1)
cnt=0


for i in range(2,n+1):
    #if ch[i]==0:
    for j in range(i,n+1,i):
        if ch[j]==0:
            ch[j]=1
            cnt+=1
            if cnt==k:
                print(j)
                break
'''


