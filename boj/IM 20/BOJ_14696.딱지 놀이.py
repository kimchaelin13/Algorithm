import sys
sys.stdin=open('input.txt','r')

'''
1 4
4 3 3 2 1


sort함
#1. (4)
#2. (1 2 3 3)

둘다 리스트에 담는다

만약에 둘중에 별이 
'''
def winner(A,B):
    global flag
    if A.count(4)>B.count(4):
        return 'A'
    elif A.count(4) < B.count(4):
        return 'B'
    else:
        if A.count(3)>B.count(3):
            return 'A'
        elif A.count(3) < B.count(3):
            return 'B'
        else:
            if A.count(2)>B.count(2):
                return 'A'
            elif A.count(2) < B.count(2):
                return 'B'
            else:
                if A.count(1)>B.count(1):
                    return 'A'
                elif A.count(1)<B.count(1):
                    return 'B'
                else:
                    flag=1

for tc in range(1,int(input())+1):
    #1 4
    #4 3 3 2 1
    A=list(map(int,input().split()))[1:]
    B=list(map(int,input().split()))[1:]
    flag=0
    win=winner(A,B)
    if flag==0:
        print(win)
    else:
        print('D')