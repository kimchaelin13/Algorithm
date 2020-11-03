import sys
sys.stdin=open('input.txt','r')

N,K=map(int,input().split())

arr=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
cnt_room=0

for _ in range(N):
    s,g=map(int,input().split())

    arr[g][s]+=1
    if arr[g][s] == K:
        cnt_room+=1
        arr[g][s]=0

for e in arr[1:]:
    for n in e:
        if n !=0:
            cnt_room+=1
print(cnt_room)
