import sys
sys.stdin = open('input.txt','r')

num=['0','1','2','3','4','5','6','7','8','9']
a=input()
temp=''
for i in range(len(a)):
    if a[i] in num:
        temp+=a[i]

result=int(temp)
cnt=0
for i in range(1,result+1):
    if result%i == 0:
        cnt+=1

print(result)
print(cnt)