import sys
sys.stdin=open('input.txt','r')

N=int(input())
res=-1234
res_list=[]
for i in range(N+1):
    temp=[N,i]
    while True:
        a=temp[-2]-temp[-1]
        temp.append(a)
        if a<=-1:
            break

        if len(temp)>res:
            res=len(temp)
            res_list=temp[:]

print(res)
print(*res_list)
