import sys
sys.stdin=open('input.txt','r')
n=int(input())
bulb=list(map(int,input().split()))
bulb.insert(0,0)

for _ in range(int(input())):
    sex,num=map(int,input().split())

    if sex==1:
        for i in range(1,n):
            if i%num==0:
                if bulb[i]==0:
                    bulb[i]=1
                else:
                    bulb[i]=0
    if sex==2:
        x=0
        y=0
        while True:
            if bulb[num-1+x]==bulb[num+1+y]:
                if bulb[num-1+x]==1:
                    bulb[num-1+x]=bulb[num+1+y]=0
                else:
                    bulb[num-1+x]=bulb[num+1+y]=1
                x=x-1
                y=y+1
            else:
                if bulb[num]==1:
                    bulb[num]=0
                    break
                else:
                    bulb[num]=1
                    break
print(*bulb[1:])