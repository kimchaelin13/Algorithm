import sys
sys.stdin = open('input.txt','r')

'''
10 3
3 -2 -4 -9 0 3 7 13 8 -3

이중 FOR문으로 풀어야함
[3 -2 -4 -9 0 3 7 13 8 -3]

K씩 더해아함..그러면? 7번인덱스까지만 세줘야함!더하면 인덱스에러남, 그리고 res보다 크면 계속 갱신해준다

for i in range(N,10-3+1):
    for j in range(i,i+K):
        sum += list[j]

시간초과난다. 

잘 생각해보시면 2~k+1번째 수의 합은 1~k번째 수의 합에서 1번째 수를 빼고, k+1번째 수를 더한 값과 같습니다.

'''
N,K=map(int,input().split())
nums=list(map(int,input().split()))

temp=sum(nums[:K])
res=temp
#print(temp)
for i in range(K,N):
    temp= temp+nums[i]-nums[i-K]

    if temp>res:
        res=temp
print(res)
