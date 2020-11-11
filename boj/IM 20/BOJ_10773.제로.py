import sys
sys.stdin=open('input.txt','r')

'''
10만큼 돌면서
0이 나오면 가장 뒤에 있는 요소를 pop하고
아니면 계속 어펜드한다.
'''
N=int(input())
li=[]
for _ in range(N):
    a=int(input())
    if a!=0:
        li.append(a)
    else:
        li.pop()
print(sum(li))