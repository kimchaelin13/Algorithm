import sys
sys.stdin=open('input.txt','r')
def dist_calc(dir,pos):
    if dir==1:
        #북
        return pos
    elif dir==2:
        #남
        return garo+sero+garo-pos
    elif dir==3:
        #서
        return garo+sero+garo+sero-pos
    else:
        #동
        return garo+pos
garo,sero=map(int,input().split())
dist=[]
N=int(input())
for _ in range(N+1):
    dir,pos=map(int,input().split())
    dist.append(dist_calc(dir,pos))

ans=0
for i in range(N):
    clockwise = abs(dist[i]-dist[-1])
    ans += min(clockwise, (2*(garo+sero) - clockwise))
print(ans)