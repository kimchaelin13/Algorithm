import sys
sys.stdin = open("input2.txt", "r")

for tc in range(1,11):
    N=int(input())
    ladder=[list(map(int,input().split())) for _ in range(100)]
    dx=ladder[99].index(2) #99번리스트에서(마지막줄) 값이 2인 index를 찾아라!, 리스트는 find 못씀
    dy=99
    move=0

    while dy>0:
        #left
        if (move==3 or move==1) and dx>0 and ladder[dy][dx-1]==1:
            move=1
            dx-=1
        #right
        elif (move==3 or move==2) and dx<99 and ladder[dy][dx+1]==1:
            move=2
            dx+=1
        #up
        else:
            move=3
            dy-=1

    print('#{} {}'.format(tc,dx))