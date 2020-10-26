import sys
sys.stdin = open("input.txt", "r")


for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    sequence=list(map(int,input().split()))

    for i in range(M):
        sequence.append(sequence[0])
        sequence.pop(0)

    print('#{} {}'.format(tc,sequence[0]))



