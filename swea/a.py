import sys
sys.stdin=open('input.txt','r')
tc=int(input())
for tc in range(1,tc+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    #print(arr)
    total=[]
    for i in range(N):
        middle=N//2
        if i<middle:
            total.extend(arr[i][middle-i:middle+i+1])
        elif i==middle:
            total.extend(arr[i][:])
        else:
            total.extend(arr[i][i-middle:middle-i])
            ===