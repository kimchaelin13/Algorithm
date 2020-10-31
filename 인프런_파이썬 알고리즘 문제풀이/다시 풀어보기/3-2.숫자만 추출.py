import sys
sys.stdin=open('input.txt','r')

nums=['0','1','2','3','4','5','6','7','8','9']

num=''
s=input()

#숫자만 추출하기
for i in s:
    if i in nums:
        num+=i
num=int(num)
print(num)

#약수의 개수 출력하기
cnt=0
for i in range(1,num+1):
    if num%i==0:
        cnt+=1
print(cnt)