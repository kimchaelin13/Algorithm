import sys
sys.stdin=open('input.txt','r')

'''
10
5
2 1 0 1 (+ -  * /)
3 5 3 7 9

#1 +2개 -1개 /1개로 만들수있는 모든 순열을 다구한다
#2.순열 한개 구하면 거기에 숫자 끼워넣어서 => 숫자 하나 만들고 res에 넣고 

'''
#내가 만들 프로그램은 넘버와 연산자로 계산해서 max,min을 계속 갱신하다가 답을 리턴하는것!
def make_number(L,total):
    global MAX,MIN
    if L==len(operator)-1:
        if MAX<total:
            MAX=total
        if MIN>total:
            MIN=total

    else:
        for i in range(4):
            if operator[i]:
                operator[i]-=1
                if i==0:
                    total += nums[i+1]
                elif i==1:
                    total -= nums[i+1]
                elif i==2:
                    total *= nums[i+1]
                else:
                    total = int(total/nums[i+1])
                make_number(L+1,total)
                operator[i]+=1


for tc in range(1,int(input())+1):
    N=int(input())
    operator=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    MAX=-987654321
    MIN=987654321
    make_number(0,nums[0])
    print('#{} {}'.format(tc,MAX-MIN))


# for tc in range(1,int(input())+1):
#     N=int(input())
#     yeonsan=[]
#     for _ in range(4):
#         yeonsan.append(list(map(int,input().split())))
#     number=list(map(int,input().split()))



# def make_operator(L):
#     global ans,MAX,MIN
#     if L==len(operator):
#         MAX = max(MAX,cal(number,res))
#         MIN = min(MIN,cal(number,res))
#
#     else:
#         for i in range(N-1):
#             if check[i]==0:
#                 check[i]=1
#                 res[L]=operator[i]
#                 make_operator(L+1)
#                 check[i]=0
#
# def cal(number,res):
#     total=number[0]
#     for i in range(0,len(res)):
#         if res[i]=='+':
#             total+=number[i+1]
#         elif res[i]=='-':
#             total-=number[i+1]
#         elif res[i]=='*':
#             total *= number[i+1]
#         elif res[i] =='/':
#             total = int(total/res[i+1])
#     return total
#
# for tc in range(1,int(input())+1):
#     N=int(input())
#     MAX=-987654321
#     MIN=987654321
#     temp=[]
#     plus,minus,multiple,divide=input().split()
#     number = list(map(int, input().split()))
#     temp.extend((plus,minus,multiple,divide))
#     operator=[]
#     a=['+','-','*','/']
#     s=0
#     for i in range(s,4):
#         for j in range(s,4):
#             operator += a[j]*int(temp[i])
#             s+=1
#             break
#     print(operator)
#     #가능한 순열 만들기
#     check=[0]*(N-1)
#     res=[0]*(N-1)
#     ans=[]
#     make_operator(res,arr)
#     #print(number)