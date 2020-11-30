import sys
sys.stdin=open('input (55).txt','r')

'''
2 2 2
3 4
손님 오름차순 정렬 
가장 늦게 오는 손님까지 붕어빵 번호 만듦 -> [0,0,2,0,2]

3초사람 살 수 있는지? 3 인덱스 확인 -> 0이라면 살수있음
                                  0이 아니라면 그 앞의 인덱스를 확인하면서, 0이 아닌게 나온다면 살수있음
                                                                    그리고 그 인덱스 벨류값 -=1
'''

for tc in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    guest = sorted(list(map(int,input().split())))
    bread=[]
    for i in range(max(guest)+1):
        if i>=M and i%M==0:
            bread.append(K)
        else:
            bread.append(0)
    #print(bread)
    res=0
    flag=0
    for k in guest:
        if bread[k]!=0:
            res+=1
            bread[k]-=1
        else:
            for j in range(k,-1,-1):
                if bread[j]>0:
                    res+=1
                    bread[j]-=1
                    flag=1
                    break
    ans=''
    if res==len(guest):
        ans='Possible'
    else:
        ans='Impossible'
    print('#{} {}'.format(tc,ans))