import sys
sys.stdin=open('input.txt','r')


W=sorted(input().upper())
cnt=1
MAX=0
MAX_W=0
i=0
flag=0
while i<len(W):
    #다르면 갱신해주거나 아니면 끝까지 갔으면 그전까지 센 값을 비교해야하므로
    if (i+1==len(W)) or (W[i]!=W[i+1]):
        if cnt>=MAX:
            flag=0
            if cnt == MAX:
                flag = 1
            MAX=cnt
            MAX_W=W[i]
            cnt=1
        cnt=1
    else:
        cnt+=1
    i+=1

if flag==0:
    print(MAX_W)
else:
    print('?')

