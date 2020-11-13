import sys
sys.stdin=open('input.txt','r')

'''
남자 

'''
def male(bulb,num):
    for i in range(num,N+1,num):
        if bulb[i]==1:
            bulb[i]=0
        else:
            bulb[i]=1
    return bulb

def female(bulb,num):
    #이 함수 인덱스
    s=1
    while True:
        if num-s==0 or num+s==N+1:
            break
        elif (bulb[num-s] != bulb[num+s]):
            break
        s+=1
    s-=1
    for i in range(num-s,num+s+1):
        if bulb[i]==0:
            bulb[i]=1
        else:
            bulb[i]=0
    return bulb

if __name__ == '__main__':
    N=int(input())
    bulb=list(map(int,input().split()))
    bulb.insert(0,0)
    for _ in range(int(input())):
        sex,num=map(int,input().split())
        if sex==1:
            bulb=male(bulb,num)
        elif sex==2:
            bulb=female(bulb,num)
    for idx in range(1,N,20):
        print(*bulb[idx:idx+20])