import sys
sys.stdin = open("input.txt", "r")
def inOrder(v):
    #왼쪽자식이 있을때, 무조건 왼쪽으로 내려가면서
    if len(arr[v]) >= 3:
        inOrder(int(arr[v][2]))
    #출력
    print(arr[v][1],end="")
    #오른쪽 자식 있을때
    if len(arr[v])==4:
        inOrder(int(arr[v][3]))

for tc in range(1,11):
    N=int(input())

    #2차원리스트로 인접리스트느낌으로 처리
    arr=[[]] #0번 인덱스 버리기

    for i in range(N):
        #문자열 리스트형태로 담음
        arr.append(input().split()) #[W,2,3]
    print(arr)

    print('#{}'.format(tc),end=" ")
    inOrder(1)
    print()

