import sys
sys.stdin=open('input.txt','r')
'''
(내기 지금 있는 곳 + (가고자 하는 val)) % (인덱스 전체 길이) 로 가서 +1를 해준다
'''
N,M,L=map(int,input().split())
score=[0]*N
score[0]=1
s=0
flag=0
while True:
    if score[s]==M:
        break
    for i in range(s,N):
        #공을 받은 횟수가 홀수면
        if score[i] % 2:
            score[(i+L)%N]+=1
            s=(i+L)%N
            break
        #공을 받은 횟수가 짝수면
        else:
            score[(i-L)%N]+=1
            s=(i-L)%N
            break
print(sum(score)-1)