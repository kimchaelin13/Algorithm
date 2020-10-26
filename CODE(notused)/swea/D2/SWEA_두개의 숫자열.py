import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    int1=list(map(int,input().split()))
    int2=list(map(int,input().split()))
    A=len(int1)
    B=len(int2)
    #위에가 움직임. 아래는 가만히 있음. 그러면 완전탐색느낌으로 풀고싶당
    total=[]
    for i in range(B-A+1):
        sub_total=0
        for j in range(A):
            sub_total

