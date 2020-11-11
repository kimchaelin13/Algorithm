import sys
sys.stdin=open('input.txt','r')

'''
리스트 준비
[(1,3),(2,1),(3,4),(4,3),(5,2)] 로 받기

'''

N=int(input())
line=[]
info=list(map(int,input().split()))
for i in range(1,N+1):
    line.append((i,info[i-1]))
line.sort(key=lambda x:(x[1],x[0]))
temp=0
res=0
for j in range(N):
    temp += line[j][1]
    res += temp
print(res)