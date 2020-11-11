import sys
sys.stdin=open('input.txt','r')


for tc in range(4):
    x1,y1,x2,y2,xx1,yy1,xx2,yy2=map(int,input().split())

    #떨어져있음 => d
    if (x2 < xx1 or y2<yy1) or (xx2<x1 or yy2<y1):
        print('d')
    elif (xx1==x2 and y2==yy1) or (x1==xx2 and y1==yy2) or (xx1==x2 and yy2==y1) or (x1==xx2 and yy1==y2):
        print('c')
    #선분
    elif (xx1==x2) or (y1==yy2) or (x1==xx2) or (y2==yy1):
        print('b')
    else:
        print('a')