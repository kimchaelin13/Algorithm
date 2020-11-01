import sys
sys.stdin=open('input.txt','r')

def rotation(arr):
    tmp=[['']*N for _ in range(N)]

    #회전_90도
    for r in range(N):
        for c in range(N):
            tmp[c][N-1-r]=arr[r][c]
    return tmp

def result(arr,col):
    for r in range(N):
        for c in range(N):
            ans[r][col] += arr[r][c]


if __name__=='__main__':
    for tc in range(1,int(input())+1):
        N=int(input())
        arr=[input().split() for _ in range(N)]
        #print(arr), [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        ans=[['']*3 for _ in range(N)]
        #print(ans)  [['', '', ''], ['', '', ''], ['', '', '']] 이렇게 출력
        for i in range(3):
            arr= rotation(arr) #그럼 여기 arr에 tmp가 되겠구나
            result(arr,i)

        #print(ans)
        print('#{}'.format(tc))
        for i in range(N):
            for j in range(3): #열은 90,180,270이니까 3개만
                print(ans[i][j], end=" ")
            print()