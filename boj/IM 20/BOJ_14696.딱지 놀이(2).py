import sys
sys.stdin=open('input.txt','r')

def count_arr(info):
    arr=[0]*5
    #4 3 3 2 1, 3을 발견함 -> arr[3]+=1
    for i in info[1:]:
        arr[i]+=1
    return arr

def battle():
    global flag
    if A[4]>B[4]:
        return 'A'
    elif A[4]<B[4]:
        return 'B'
    else:
        if A[3]>B[3]:
            return 'A'
        elif A[3]<B[3]:
            return 'B'
        else:
            if A[2]>B[2]:
                return 'A'
            elif A[2]<B[2]:
                return 'B'
            else:
                if A[1]>B[1]:
                    return 'A'
                elif A[1]<B[1]:
                    return 'B'
                else:
                    flag=1

for tc in range(int(input())):
    A_info=list(map(int,input().split()))
    B_info=list(map(int,input().split()))
    A=count_arr(A_info)
    B=count_arr(B_info)
    flag=0
    win=battle()
    if flag==0:
        print(win)
    else:
        print('D')