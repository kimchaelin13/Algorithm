import sys
sys.stdin=open('input.txt','r')







'''
시간 초과 

def selection(res):
    n=len(res)

    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if res[j] < res[min]:
                min=j
        res[min],res[i]=res[i],res[min]

    return res

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
res=[]
for i in A:
    res.append(i)
for i in B:
    res.append(i)
print(*selection(res))

'''

'''
#통과
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
res=[]
for i in A:
    res.append(i)
for i in B:
    res.append(i)
print(*sorted(res))

'''

N,M=map(int,input().split())
AB=list(map(int,input().split()))+list(map(int,input().split()))
print(' '.join(map(str,sorted(AB))))