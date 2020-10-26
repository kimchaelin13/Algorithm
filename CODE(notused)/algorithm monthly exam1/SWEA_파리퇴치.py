import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    flies=[list(map(int,list(input().split()))) for _ in range(N)]

    killed=[]
    for i in range(N-M+1):
        for j in range(N-M+1):
            total=0
            for m in range(M):
                total+=sum(flies[i+m][j:j+M])
            killed.append(total)
    print(max(killed))

