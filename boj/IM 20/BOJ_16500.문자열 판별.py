import sys
sys.stdin=open('input.txt','r')

'''
#1.단어목록리스트에 단어를 담는다
#2.처음 시작하는 단어가 단어목록안에 있는 첫번째와 같다면? 
    만약 그 단어 == 자른 전체 단어
    인덱스+= 그 단어의 길이
'''
T=input()
A=[]
for _ in range(int(input())):
    A.append(input())

s=0
res=1
flag=0
for i in A:
    while s<len(T):
        if T[s]==i[0]:
            if T[s:s+len(i)]==i:
                s += len(i)
            else:
                res=0
                flag=1
                break
    if flag:
        break
print(res)