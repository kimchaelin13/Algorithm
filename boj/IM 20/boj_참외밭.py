import sys
sys.stdin=open('input.txt','r')
'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''
N=int(input())
info=[]
for _ in range(6):
    dir,val = map(int,input().split())
    info.append(val)
MAX,pos=0,0
for i in range(0,len(info)-1):
    if info[i]*info[i+1] > MAX:
        MAX=info[i]*info[i+1]
        pos=i

MIN = info[(pos+3)%6] * info[(pos+4)%6]

res = (MAX-MIN)*N
print(res)