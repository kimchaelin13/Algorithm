import sys
sys.stdin=open('input.txt','r')

'''
왼쪽 꼭지점에서 시계방향으로 그 위치에 있는 거리까지 구하는 방법
북:value
님:가로+세로+가로-val
서:가로+세로+가로+세로-val
동:가로+val

시계방향으로 왼쪽위꼭지점부터 모든 dist를 구하고,
시계방향거리는 = 내위치거리 - 해당위치 거리
반시계방향 거리는 = 전체둘레-시계방향 거리
둘중작은걸 더함

10 5
3
1 4
3 2
2 8
2 3
'''
def check(dir,val):
    #북
    if dir==1:
       return val
    #남
    elif dir==2:
        return N+M+N-val
    #서
    elif dir==3:
        return N+M+N+M-val
    #동
    else:
        return N+val
N,M=map(int,input().split())
n=int(input())
info=[]
for _ in range(n+1):
    dir,val=map(int,input().split())
    info.append((dir,val))

dist_info=[]
for dir,val in info:
    dist_info.append(check(dir,val))
#print(dist_info)
ans=0
for i in range(n):
    res_1 = abs(dist_info[i]-dist_info[-1])
    #print('1',res_1)
    res_2 = 2*(N+M) - res_1
    #print('2',res_2)
    ans += min(res_1,res_2)

print(ans)