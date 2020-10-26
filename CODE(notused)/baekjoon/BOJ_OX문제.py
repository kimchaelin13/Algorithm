import sys
sys.stdin = open("input.txt", "r")

for _ in range(int(input())):
    ox=list(input())
    result=[0]*len(ox)
    cnt=0
    for i in range(len(ox)):
        if ox[i]=='O':
            cnt+=1
            result[i]=cnt
        else:
            cnt=0
            result[i]=cnt
    print(sum(result))