import sys
sys.stdin=open('input.txt','r')


'''
16의 약수는 1,2,4,8,16 / len(s)//2 => 4*4
(8의 약수는 1,2,4,8 / len(s)//2 = m (m-1) = r이고 m이 c다.
'''

S=input()
N=len(S)
yaksu=[]
for i in range(1,N+1):
    if N%i ==0:
        yaksu.append(i)
#print(yaksu)
#약수의 길이가 홀수면
if len(yaksu)%2:
    R,C=yaksu[len(yaksu)//2],yaksu[len(yaksu)//2]
else:
    R,C=yaksu[(len(yaksu)//2)-1],yaksu[(len(yaksu)//2)]

arr=[['']*C for _ in range(R)]
#print(arr)

#2.채워넣기
#boudonuimilcbsai
s=0
for c in range(C):
    for r in range(R):
        arr[r][c]=S[s]
        s+=1
for r in range(R):
    for c in range(C):
        print(arr[r][c],end="")