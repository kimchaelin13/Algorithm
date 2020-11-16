import sys
sys.stdin=open('input.txt','r')



'''
5
0 1 1 3 2
'''

N=int(input())
n=list(map(int,input().split()))
line=[]

for i in range(N):
    line.insert(n[i],i+1)

line.reverse()
print(*line)