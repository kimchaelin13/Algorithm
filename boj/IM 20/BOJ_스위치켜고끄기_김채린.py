import sys
sys.stdin=open('input.txt','r')

'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3


'''

def male(bulb,idx):
    for i in range(idx,N+1,idx):
        bulb[i] = (bulb[i]+1)%2
    return bulb

def female(bulb,idx):
    size=0
    while True:
        if 1<=idx-size<=N and 1<=idx+size<=N and bulb[idx-size] == bulb[idx+size]:
            ch = (bulb[idx-size]+1)%2
            bulb[idx-size], bulb[idx+size] = ch,ch
            size+=1
        else:
            break
    return bulb

N=int(input())
bulb=[0]+list(map(int,input().split()))

for _ in range(int(input())):
    gen,idx = map(int,input().split())
    if gen == 1:
        bulb = male(bulb,idx)
    else:
        bulb = female(bulb,idx)

for i in range(1,N,20):
    print(*bulb[i:i+20])