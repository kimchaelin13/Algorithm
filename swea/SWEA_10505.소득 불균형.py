import sys
sys.stdin=open('input.txt','r')

'''
3
7
15 15 15 15 15 15 15
10
1 1 1 1 1 1 1 1 1 100
7
2 7 1 8 2 8 4

#1.평균을 구하고
#2.그 평균보다 낮은 사람들을 cnt함
'''

for tc in range(1,int(input())+1):
    N=int(input())
    w=list(map(int,input().split()))
    avg=sum(w)//N
    #print(avg)
    cnt=0
    for i in range(N):
        if avg >= w[i]:
            cnt+=1
    print('#{} {}'.format(tc,cnt))