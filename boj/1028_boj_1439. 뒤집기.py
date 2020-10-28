import sys
sys.stdin=open('input.txt','r')

'''


0001100

000 가다가 만약에 1을 만나 그럼 0을 어디 res에 넣어,
0,1 인덱스 비교/1,2인덱스 비교/2,3인덱스 비교 -> 아 다르네? 그러면? n[2]를 res에 넣어줌(0을 넣은것)
3/4비교 / 4,5비교(어?다르네?) 그럼 n[4]를 넣어줌/ 5,6비교(마지막은 마지막 원소를 무조건 넣어줘야하겠네_

'''

res=[]
S=list(map(int,list(input())))

for i in range(0,len(S)-1):
    if S[i] != S[i+1]:
        res.append(S[i])
res.append(S[-1])
print(min(res.count(0),res.count(1)))


