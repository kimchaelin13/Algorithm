import sys
sys.stdin=open('input.txt','r')

N,M = map(int,input().split())

S,C=[],[]
for _ in range(N):
    S.append(input())
for _ in range(M):
    C.append(input())

'''
체크배열에서 하나 뽑아서, 
S배열에 있는 원소 하나하나 비교하면서, 만약에 포함되는 원소가 있으면! break, cnt+=1

'''
cnt=0
for i in C:
    for j in range(N):
        if i in S[j]:
            cnt +=1
            break

print(cnt)