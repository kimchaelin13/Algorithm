import sys
sys.stdin=open('input.txt','r')

''''
2번으로 했는데 됐고 1번은 틀림 

이 코드는 대체 왜 안되는걸까?,,,,
'''
#false 코드
n,k=map(int,input().split())

ch=[0]*(n+1)
cnt=0

for i in range(2,n+1):
    for j in range(i,n+1,i):
        #이미 1로 표시되어있다면? continue해서 cnt를 더하지 않는다
        if ch[j]==1:
            continue
        #0으로 표시되어있다면
        else:
            #1로 바꾸어주고
            ch[j]=1
            #cnt를 더해준다
            cnt+=1
        #그리고 cnt가 k가 됐을때 그때의 j를 프린트한다
        if cnt==k:
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


