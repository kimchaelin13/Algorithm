import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    arr = list(map(int,input().split()))
    result=[]

    for i in range(N-M+1):
        total = 0
        total+=sum(arr[i:i+M])
        result.append(total)
    print('#{} {}'.format(tc,max(result)-min(result)))

