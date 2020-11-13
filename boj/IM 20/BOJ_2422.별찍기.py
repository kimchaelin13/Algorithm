import sys
sys.stdin=open('input.txt','r')

# N=int(input())
# star=['']*(2*N-1)
# middle=(len(star)//2)
# star[middle]='*'
# print(star)
# s=1
# while True:
#     #종료조건 s-가 0되거나 e가 +됐을때
#     if middle-s<0 or middle+s==len(star):
#         break
#     star[middle-s],star[middle+s]='*','*'
#     print(star)
#     s+=1
#
N=int(input())
for i in range(1,N+1):
    res=' '*(N-i)+'*'*((2*i)-1)
    print(res)