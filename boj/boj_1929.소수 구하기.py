import sys
sys.stdin=open('input.txt','r')

'''
3,16

에라테 어쩌고 체로 n이상 3이하의 소수 배열을 만듦(소수면 0이고 아니면 1로 채울거야)
그다음에 그걸 그대로 프린트하자


'''
import sys
M,N=map(int,sys.stdin.readline().split())
#이렇게 ch[1]=1도 초기화해줘야 하는데, 이유는 만약에
#check=[0]*(N+1)로 하면, ch[1]=0이다. 그래서 만약에 M이 1이면 1도 같이 소수라고 한다!
check=[1,1]+[0]*(N+1)

#소수배열만들기
for i in range(2,N+1):
    for j in range(i+i,N+1,i):
        check[j]=1

#소수만 뽑기
for k in range(M,N+1):
    if check[k]==0:
        print(k)