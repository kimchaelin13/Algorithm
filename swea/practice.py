'''
1. 90도, 180도, 270도를 구해야하는데 90도만 하고 계속 반복하게 하면 됨///
2. 주어진 행렬을 rotate할 함수 한개
3. 마지막에 출력할 함수에 N*3 배열에 집에넣어주는 함수

'''
import sys
sys.stdin=open('input.txt','r')

def rotate(arr):
    tmp=[['']*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            tmp[c][N-1-r]=arr[r][c]
    return tmp

def result(arr,col):
    for r in range(N):
        for c in range(N):
            ans[r][col]+=arr[r][c]
    return ans



if __name__=='__main__':
    for tc in range(1,int(input())+1):
        N=int(input())
        #왜 문자열로 받냐면, 이걸 나중에 다 하나씩 붙여줄건데, int로 받으면 연산이 됨
        arr=[input().split() for _ in range(N)]

        ans=[['']*3 for _ in range(N)]

        #rotate 3번 돌려야지 90도, 180도, 270도
        #그리고 ans에 하나씩 넣어야 한다.
        for i in range(3):
            arr=rotate(arr)
            ans=result(arr,i)

        print('#{}'.format(tc))
        for r in range(N):
            for c in range(3):
                print(ans[r][c],end=' ')
            print()
