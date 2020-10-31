import sys
sys.stdin=open('input.txt','r')
'''
#1.tc를 받고
#2.input()을 받고
    for i in range(len(input())//2):
        만약에 문자열안에 같은 게 있다면 둘다 지운다
    남은걸 res에 넣는다
    출력한다


#1.s=0으로 시작함,
    만약에 
'''

for tc in range(1,int(input())+1):
    s=list(input())
    s.sort()
    print(s)
    # res=[]
    # for i in range(0,len(s),2):
    #     if s[i] != s[i+1]:
    #         res


