import sys
sys.stdin=open('input.txt','r')
'''
좌표를 정렬하고, 가장 오른쪽값과 왼쪽값에 말을 한마리씩 넣어놓는다.

'''
def Count(len):
    cnt=1
    ep=line[0]
    for i in range(1,n):
        #마지막에 말을
        if line[i]-ep>=len:
            cnt+=1
            ep=line[i]
    return cnt

n,c=map(int,input().split())
line=[]
for _ in range(n):
    tmp=int(input())
    line.append(tmp)
line.sort()
lt=1 #최소거리
rt=line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
