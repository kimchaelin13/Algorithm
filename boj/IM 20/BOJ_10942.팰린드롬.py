import sys
sys.stdin=open('input.txt','r')

'''
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
'''

N=int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())

for _ in range(q):
    s,e=map(int,sys.stdin.readline().split())
    c = (e - s + 1) // 2
    s,e = s-1,e-1
    ANS = 1

    en = e
    st = s
    for i in range(c):
        if nums[st] != nums[en]:
            ANS = 0
            break
        st +=1
        en -=1
    print(ANS)