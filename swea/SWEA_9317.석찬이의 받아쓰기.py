'''
2
16
MyNameIsSeokChan
mynameisseokchan

정답을 s로 받고,
stack=[]
만약에 같으면 stack에 집어넣고,

'''
import sys
sys.stdin=open('input.txt','r')
for tc in range(1,int(input())+1):
    N=int(input())
    answer=input()
    chan=input()
    cnt=0
    for i in range(N):
        if chan[i]==answer[i]:
            cnt+=1
    print('#{} {}'.format(tc,cnt))