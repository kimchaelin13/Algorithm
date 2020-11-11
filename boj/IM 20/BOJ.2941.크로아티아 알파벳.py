import sys
sys.stdin=open('input.txt','r')

'''
ljes=njak


'''
C=['c=','c-','dz=','d-','lj','nj','s=','z=']
S=input()
s=0
cnt=0
#2개짜리일때
while s<=len(S)-1:
    if S[s:s+1+1] in C:
        cnt+=1
        s+=2
    elif S[s:s+1+1+1] in C:
        cnt+=1
        s+=3
    else:
        cnt+=1
        s+=1
print(cnt)



l=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=input()
for i in l:
    a=a.replace(i,' ')
print(len(a))
