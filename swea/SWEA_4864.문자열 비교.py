import sys
sys.stdin=open('input.txt','r')

for tc in range(1,int(input())+1):
    s1=input()
    s2=input()
    N=len(s1)
    M=len(s2)
    res=0
    for i in range(M-N+1):
        if s2[i:i+N]==s1:
            res=1
    print('#{} {}'.format(tc,res))

# s1='abcde'
# print(s1[0:4])
