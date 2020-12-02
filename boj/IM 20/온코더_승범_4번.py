import sys
sys.stdin=open('input.txt','r')

'''
5
21378
31378
11111101
50005
26227174957722514961366
'''
cardnum=input()
result = 0
length = len(cardnum)
#length & 1 => 1이 나옴, 짝수이면? 이라는 조건인가
if not length & 1:
    cardnum = '0' + cardnum
for i in range(len(cardnum)):
    num = int(cardnum[i])
    a = 0
    if i & 1:
        a += (num * 2)
    else:
        a += num
    if a >= 10:
        result += (a % 10); result += 1
    else:
        result += a
if result % 10:
    print('INVALID')
else:
    print('VALID')

# for tc in range(1,int(input())+1):
#     N=list(map(int,input()))
#     ans=0
#     if len(N)%2:
#         for h in range(len(N)):
#             if h%2:
#                 N[h]=N[h]*2
#             if N[h]<10:
#                 ans += N[h]
#             else:
#                 ans += (N[h]%10) + 1
#     else:
#         for e in range(len(N)):
#             if e%2==0:
#                 N[e]=N[e]*2
#             if N[e]<10:
#                 ans+=N[e]
#             else:
#                 ans += (N[e]%10)+1
#
#     if ans%10:
#         print('#{} {}'.format(tc,'INVALID'))
#     else:
#         print('#{} {}'.format(tc,'VALID'))