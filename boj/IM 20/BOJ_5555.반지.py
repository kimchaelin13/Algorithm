import sys
sys.stdin=open('input.txt','r')

'''
#1. 입력받을때 똑같은걸 2개 이어붙여서 받음
#2. 전체길이-찾아야하는 길이+1까지 돌고, 찾아야하는게 나오면 브레잌, 카운트센다
'''

s=input()
cnt=0
for _ in range(int(input())):
    S=input()
    S = S*2
    for i in range(len(S)-len(s)+1):
        if S[i:i+len(s)] == s:
            cnt+=1
            break
print(cnt)