import sys
sys.stdin=open('input.txt','r')

n=int(input())
body=[]
for _ in range(n):
    h,w=map(int,input().split())
    body.append((h,w))
body.sort(reverse=True) #내림차순 정렬하면 키는 볼필요가없고,몸무게만 최댓값을 구한다고 생각하면 됨
#몸무게의 기존 최대값이 갱신되면 cnt+=1


largest=0
cnt=0
for h,w in body:
    if w>largest:
        largest=w
        cnt+=1
print(cnt)
