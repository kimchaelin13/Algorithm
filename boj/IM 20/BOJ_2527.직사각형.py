import sys
sys.stdin=open('input.txt','r')

'''
3 10 50 60 100 100 200 300
'''

for _ in range(4):
    res=''
    x,y,xx,yy,x2,y2,xx2,yy2=map(int,input().split())
    if (x2>xx) or (yy<y2) or (x>xx2) or (y>yy2):
        res='d'
    elif (xx==x2 and yy==y2) or (x==xx2 and y==yy2) or (xx==x2 and y==yy2) or (x==xx2 and y2==yy):
        res='c'
    elif (yy==y2) or (x2==xx) or (y==yy2) or (x==xx2):
        res='b'
    else:
        res='a'
    print(res)