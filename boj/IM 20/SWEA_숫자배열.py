import sys
sys.stdin=open('input.txt','r')


def rotate(arr):
    temp_90=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_90[j][N-1-i]=arr[i][j]
    return temp_90

def result(temp):
    for r in range(N):
        ADD = ''
        for c in range(N):
            ADD += str(temp[r][c])
        res[r][i] = ADD
    return res

for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    temp_90 = arr
    res = [[''] * N for _ in range(N)]

    for i in range(3):
        temp_90 = rotate(temp_90)
        res = result(temp_90)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(res[i][j],end=" ")
        print()