import sys
sys.stdin=open('input.txt','r')

def is_palindrome(line):
    if line!=line[::-1]:
        return False
    return True

for tc in range(1,11):
    N=int(input())
    arr=[list(map(str,input())) for _ in range(8)]
    arr += list(map(list,zip(*arr)))
    cnt=0
    for line in arr:
        for i in range(8-N+1):
            if is_palindrome(line[i:i+N]):
                cnt+=1
    print('#{} {}'.format(tc,cnt))