import sys
sys.stdin=open('input.txt','r')

'''
5
2 4 5 1 3

#1. 리스트 입력받고 
#2. list[0],list[-1] 해야하는데
    더 작은걸 res에 넣는다
    넣고나면 넣은건 pop
#3. 



'''

n=int(input())
a=list(map(int,input().split()))
#양끝을 가리키는 두 포인터변수(왼,오)
lt=0
rt=n-1
#배열의 마지막 value
last=0
res=''
tmp=[]

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort() #튜플의 첫자료에 의해 정렬함
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0]