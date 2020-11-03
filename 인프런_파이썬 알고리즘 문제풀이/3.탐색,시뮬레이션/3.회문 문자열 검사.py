import sys
sys.stdin=open('input.txt','r')

n=int(input())
for tc in range(1,n+1):
    s=input()
    s=s.upper()
    size=len(s)

    for j in range(size):
        if s[j] != s[-1-j]:
            print('#{} {}'.format(tc,'NO'))
            break
    else:
        print('#{} {}'.format(tc,'YES'))




