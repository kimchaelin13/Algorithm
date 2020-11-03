import sys
sys.stdin=open('input.txt','r')

S1,S2=input(),input()
S1='0'+S1
S2='0'+S2
N,M=len(S1),len(S2)
arr=[[0]*(N) for _ in range(M)]
#print(arr)
for i in range(1,N):
    for j in range(1,M):
        if S1[i]==S2[j]:
            arr[j][i]=arr[j-1][i-1]+1
        else:
            arr[j][i]=max(arr[j][i-1],arr[j-1][i])

MAX=0
for i in range(N):
    for j in range(M):
        if arr[j][i]>MAX:
            MAX=arr[j][i]
print(MAX)