import sys
sys.stdin=open('input.txt','r')

'''
level
moon

s=0
e=끝-1

둘이 비교해서 같으면 s=1, e-=1 로 간다
그리고 s=e가 같아지면 stop, 그때 yes
'''

for tc in range(1,int(input())+1):
    ans='NO'
    word = input().upper()
    s = 0
    e = len(word) - 1
    for i in range(len(word)//2):
        if word[s] != word[e]:
            print('#{} {}'.format(tc,'NO'))
            break
        s+=1
        e-=1
    else:
        print('#{} {}'.format(tc,'YES'))
