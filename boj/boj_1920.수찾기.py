import sys
sys.stdin=open('input.txt','r')

'''
2중 for문

dab=[]
tst=[]


'''
'''
N=int(input())
dab=list(map(int,input().split()))
M=int(input())
tst=list(map(int,input().split()))

for i in range(M):
    if tst[i] in dab:
        print(1)

    else:
        print(0)
'''

N=int(input())
dab=list(map(int,input().split()))
dab.sort()
M=int(input())
tst=list(map(int,input().split()))

for i in tst:
    start=0
    end=N-1
    answer=0
    target=i
    while (start<=end):
        mid=(start+end)//2
        if dab[mid] == target:
            answer=1
            break
        elif dab[mid] > target:
            end=mid-1
        else:
            start=mid+1
    print(answer)
