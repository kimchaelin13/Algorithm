'''
대기번호가 달팽이 채우기 처럼 상, 우, 하,좌 순서로 번호가 매겨진다
여기서 좌표 x,y 는 열,행값이다!
1,1부터 방문하면서 좌표모습으로 봤을 때 우, 하, 좌 상으로 이동!
방문하지 않았으면서 배열내에서 우, 하 , 좌, 상 순으로 번호를 매기며 그 방문배열에 번호를 매기며
K번째가 됐을 때 (x,y)를 출력
'''


import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

#델타, 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]

def check(i,j):
    global num
    visited[i][j] = num
    # if num == K:
    #     return [i,j]
    # else:
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 1 or ni > R or nj < 1 or nj > C:
            continue
        if visited[ni][nj]:
            continue
        num += 1
        check(ni,nj)

#i=R, j =C
C,R = map(int,input().split())
#좌석번호
K = int(input())
#방문배열

visited = [[0]*(C+1)  for i in range(R+1)]
# pprint(visited)
num = 1

for i in range(1,R+1):
    for j in range(1,C+1):
        if visited[i][j] == False:
            check(i,j)
pprint(visited[::-1])
