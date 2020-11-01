import sys
sys.stdin = open("input.txt", "r")

#맨 아래에 2를 찾고, 사다리를 타고 올라갈거야

for test_case in range(1,11):
    test=int(input())
    ladder=[list(map(int,input().split())) for _ in range(100)]
    dy=99
    dx=ladder[99].index(2)
    move = 0
    while dy>0:
        #left, move는 1로
        if (move==3 or move==1) and dx>0 and ladder[dy][dx-1]:
            dx -=1
            move=1

        #right, move는 2로
        elif (move==3 or move==2) and dx <99 and ladder[dy][dx+1]:
            dx +=1
            move=2

        #up, move는 0으로
        else:
            dy -=1
            move=3

    print('#{} {}'.format(test_case, dx))


#조건문이 순서가 영향을 받는줄 몰랐다;


