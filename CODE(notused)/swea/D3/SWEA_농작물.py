import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N=int(input())
    farm=[list(map(int,input())) for _ in range(N)]
    total=[]
    for i in range(N):
        middle=N//2
        if i < middle:
            total.extend(farm[i][middle-i:middle+i+1])

        elif i==middle:
            total.extend(farm[i][:])

        else:
            total.extend(farm[i][i-middle:middle-i])

    print('#{} {}'.format(tc,sum(total)))