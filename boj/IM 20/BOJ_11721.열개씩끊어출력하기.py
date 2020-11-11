import sys
sys.stdin=open('input.txt','r')
S=input()
for idx in range(0,len(S),10):
    print(S[idx:idx+10])
