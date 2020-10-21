import sys
sys.stdin=open('input.txt','r')

'''
입력=20
길이가 21인 ch라는 리스트해놓음
원리는 값이 0이면 소수라고 하고 cnt+=1, 0인걸 체크하고 그걸 다 1로 바꿔줌

2는 소수다. 체크한다. 그리고 2,4,6,8,,n까지 모두 value값을 1로 변화시킨다.
그러면 그다음 3이 들어오면 3은 소수니까 체크하고, 안쪽 for문을 돌면서 1을 증가
'''

n=int(input())
ch=[0]*(n+1)
cnt=0

for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i,n+1,i): #i는 증가하는 값,2면 2씩 증가하게
            ch[j]=1
print(cnt)