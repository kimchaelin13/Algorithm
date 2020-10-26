import sys
sys.stdin = open("input2.txt", "r")

for tc in range(1,11):
    N=input()
    ladder=[list(map(int,input().split())) for _ in range(100)]
    start_xs=[i for i in range(100) if ladder[0][i]==1]
    min_cnt=99999
    ans=0

    for start_x in start_xs:
        #dx=start_x
        dy=0
        move=0
        cnt=0
        while dy < 99:
            #left
            if (move==3 or move==1) and start_x>0 and ladder[dy][start_x-1]==1:
                move=1
                start_x-=1
            #right
            elif (move==3 or move==2) and start_x<99 and ladder[dy][start_x+1]==1:
                move=2
                start_x+=1
            #down
            else:
                move=3
                dy+=1
            cnt+=1

        if min_cnt>cnt:
            min_cnt=cnt
            ans=start_x
    print('#{} {}'.format(tc,ans))