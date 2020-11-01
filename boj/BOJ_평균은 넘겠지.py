import sys
sys.stdin = open("input.txt", "r")

for _ in range(int(input())):
    tmp=list(map(int,input().split()))
    N=tmp[0]
    #print(N)
    scores=tmp[1:]
    avg=sum(scores)/N
    #print(avg)

    cnt=0
    for i in range(N):
        if scores[i]>avg:
            cnt+=1
    result=(cnt/len(scores))*100
    print("{0:2.3f}%".format(result))
#

# a=[9,100,99,98,97,96,95,94,93,91]
# print(sum(a)/len(a))