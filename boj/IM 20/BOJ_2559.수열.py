import sys
sys.stdin=open('input.txt','r')

#시간 초과
# N,K=map(int,sys.stdin.readline().split())
# arr=list(map(int,sys.stdin.readline().split()))
# res=-987654321
# for i in range(N):
#     temp=sum(arr[i:i+K])
#     if temp>res:
#         res=temp
# print(res)


'''
처음 값을 구하면, 그다음부터는 연산을 줄일수있다.
1이 처음연산값이면 그 다음은 앞에 값 현재값을 더한다.
'''
