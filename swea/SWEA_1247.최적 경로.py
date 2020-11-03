import sys
sys.stdin=open('input.txt','r')

'''
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20


집을 오름차순 정렬 (10,5),(30,10),,(90,70)

'''
import itertools
# def optimal_route(L,total,x,y):
#     global MIN
#     if total>MIN:
#         return
#     if L==N:
#         total=total+abs(x-info[2])+abs(y-info[3])
#         if MIN > total:
#             MIN=total
#     else:
#         #고객 집 개수 순열로
#         for i in range(N):
#             if check[i]==0:
#                 check[i]=1
#                 optimal_route(L+1,total+abs(x-info[i*2+4])+abs(y-info[i*2+5]),info[i*2+4],info[i*2+5])
#                 check[i]=0

def optimal_route(L,location,total):
    global MIN
    if total>=MIN:
        return
    if L==N:
        total += abs(home[0]-location[0])+ abs(home[1]-location[1])
        if total < MIN:
            MIN=total
    else:
        for i in range(N):
            if check[i]==0:
                check[i]=1
                optimal_route(L+1,client[i],total+abs(client[i][0]-location[0])+abs(client[i][1]-location[1]))
                client[i]=0
for tc in range(1,int(input())+1):
    N=int(input())
    info=list(map(int,input().split()))
    firm=(info[0],info[1])
    home=(info[2],info[3])
    client=[]
    for i in range(4,len(info),2):
        client.append((info[i],info[i+1]))
    check=[0]*N
    MIN=987654321
    optimal_route(0,firm,0)
    print('#{} {}'.format(tc,MIN))

    #temp=list(map(int,input().split()))
    #firm,home=(temp[0],temp[1]),(temp[2],temp[3])
    # client=[]

    # client.sort(key=lambda x:(x[0],x[1]))
    #permuations=itertools.permutations(client)
    #print(list(permuations))

