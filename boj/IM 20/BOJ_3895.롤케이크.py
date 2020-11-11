import sys
sys.stdin=open('input.txt','r')


'''
#1. N+1칸 배열 만들고
#2. M만큼 돌면서
    for i in range(1,M):
    x,y 받아서
    for i in range(x,y+1):
        arr[j]=i
'''
N=int(input())
M=int(input())
cake=[0]*(N+1)
exp=0
exp_num=0
real=0
real_num=0
for i in range(1,M+1):
    s,e=map(int,input().split())
    if (e-s+1) > exp:
        exp=(e-s+1)
        exp_num = i
        #가장 많은 조각을 받도록 예상되는 방청객이 여러명인 경우에는,
        #번호가 가장 작은 사람을 출력한다
        if exp_num == (e-s+1):
            exp_num = min(i,exp_num)

    for j in range(s,e+1):
        if cake[j]==0:
            cake[j]=i
# print(cake)
for m in range(1,M+1):
    temp=cake.count(m)
    if temp>real_num:
        real_num=temp
        real=m

print(exp_num)
print(real)