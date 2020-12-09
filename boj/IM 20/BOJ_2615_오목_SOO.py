'''
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1
그냥 가로, 세로 대각선2개 모두 보자
가로 dir[좌우]
세로 dir[상하]
우대각선 dir[좌하대,우하대]
좌대각선 dir[우상대,좌상대]
'''

arr = [list(map(int,input().split())) for _ in range(19)]
di = [-1,1,0,0,-1,1,-1,1]#상하좌우 좌상대 좌하대,우상대 우하대
dj = [0,0,-1,1,-1,-1,1,1]

def check(i,j,dir,num):
    visited = [[False for j in range(19)] for i in range(19)]
    visited[i][j] = True
    cnt=1
    for d in dir:
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            continue
        if arr[ni][nj] != num:
            continue
        if not visited[ni][nj]:
            cnt+=1
        i,j = ni,nj
    print('찾아라아ㅏ',cnt,i,j)
    if cnt == 5:
        return True
    else:
        return False

find = False
for i in range(19):
    for j in range(19):
        #가로 dir[좌우]
        # 세로 dir[상하]
        # 우대각선 dir[좌상대,우하대]
        # 좌대각선 dir[우상대,좌하대]
        if arr[i][j]:
            flag = False
            d = -1
            start = [i,j]
            num = arr[i][j]
            # 가로
            if check(i,j,[2,3],num):
                print(num)
                # print(start)
                print(start[0]+1,start[1]+1)
                find = True
                break
            #세로
            if check(i,j,[0,1],num):
                print(num)
                # print(start)
                print(start[0]+1,start[1]+1)
                find = True
                break
            #좌대각선
            if check(i,j,[4,5],num):
                print(num)
                # print(start)
                print(start[0]+1,start[1]+1)
                find = True
                break
            #우대각선
            if check(i,j,[6,7],num):
                print(num)
                # print(start)
                print(start[0]+1,start[1]+1)
                find = True
                break
    if find:
        break

if not find:
    print(0)