import sys
sys.stdin=open('input.txt','r')

'''
#1.입력을 받는다(int로 변환x)
#2.col이 3인 res를 만든다.
#3.3번 돌건데, 첫번째 90도 돌린 함수를 arr에 다시 갱신하고,
    res에 우겨넣을 함수를 하나 더 만든다
    for i in range(3):
        arr=rotate(arr)
        res=result(arr,i)
    이렇게 해서 i 한번 돌때마다 세로줄이 완성되게함
'''


def rotate(arr):
    temp=[['']*N for _ in range(N)]
    for r  in range(N):
        for c in range(N):
            temp[c][N-1-r]=arr[r][c]
    return temp

def result(arr,col):
    for r in range(N):
        for c in range(N):
            res[r][col]+=arr[r][c]
    return res

for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(input().split()) for _ in range(N)]
    #res에 다 우겨넣을것..
    res=[['']*3 for _ in range(N)]


    for i in range(3):
        arr=rotate(arr) #90도 돌려서 arr을 갱신하고
        res=result(arr,i) #result돌려서 0col 채우고, 1col채우고, 2col채우고
    print('#{}'.format(tc))
    for r in range(N):
        for c in range(3):
            print(res[r][c],end=" ")
        print()
