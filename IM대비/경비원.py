import sys
sys.stdin=open('input.txt','r')



def dist_calc(idx,pos):
    if idx==1:
        return pos

    elif idx==2:
        return C+R+C-pos

    elif idx==3:
        return C+R+C+R-pos
    else:
        return C+pos

C,R=map(int,input().split())
circumference= (C+R)*2

N=int(input())
for i in range(N+1):
    idx,pos = map(int,input().split())
    dist.append(dist_calc(inx,pos))

my_dist=dist[-1]

ans=0

for i in range(N):
    clockwise=abs(my_dist-dist[i])
    ans += min(clockwise,circumference-clockwise)
print(ans)