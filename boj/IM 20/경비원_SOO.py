'''
10 5
3
1 4
3 2
2 8
2 3
'''

def move(dir,d):
    ans = 0
    # 북
    if dir == 1:
        ans = d
    # 남
    elif dir == 2:
        ans = N+M+N-d
    # 서
    elif dir == 3:
        ans = N+M+N+M-d
    # 동
    else:
        ans = N+d
    return ans


N,M = map(int,input().split())
store = int(input())
info = []
for  _ in range(store):
    dir,d = map(int,input().split())
    ans = move(dir,d)
    info.append(ans)
dong = list(map(int,input().split()))
me = move(dong[0],dong[1])
# print(info,me)
all = (N+M)*2
MIN = 0
for i in info:
    ans = abs(me-i)
    # print(ans)
    MIN += min(ans,all-ans)
print(MIN)