import sys
sys.stdin=open('input.txt','r')

'''
이름의 길이가 짧을수록 이 앞에 있었고, 같은 길이면 사전 순으로 앞에 있었다
모든 이름을 다시 정리하고 같은 이름은 하나만 남겨놓기로 한 염라대왕을 도와주자.

'''


for tc in range(1,int(input())+1):
    N=int(input())
    name=set()
    for _ in range(N):
        s=input()
        name.add(s)
    print('#{}'.format(tc))
    for x in sorted(name):
        print(x)