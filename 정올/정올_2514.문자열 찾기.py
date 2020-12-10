import sys
sys.stdin=open('input.txt','r')

S=input()
cnt_1,cnt_2=0,0
for i in range(0,len(S)-3+1):
    if S[i:i+3] == 'KOI':
        cnt_1+=1
    elif S[i:i+3] == 'IOI':
        cnt_2+=1
print(cnt_1,cnt_2,sep='\n')