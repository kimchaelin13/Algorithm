'''
5 140
90 50 70 100 60

#1.오름차순 정렬
#2.for문을 돌면서
    만약에 첫번째와 마지막<=140:
        cnt+=1
        둘다 리스트에서 팝해서 없애버림
    else:
        마지막만 팝하고
        cnt+=1

'''
import sys
sys.stdin=open('input.txt','r')
N,M=map(int,input().split())
ppl=list(map(int,input().split()))
ppl.sort()

cnt=0
while len(ppl)!=0:
    if ppl[0]+ppl[-1]<=M:
        cnt+=1
        ppl.pop()
        ppl.pop(0)
    else:
        ppl.pop()
        cnt+=1
print(cnt)