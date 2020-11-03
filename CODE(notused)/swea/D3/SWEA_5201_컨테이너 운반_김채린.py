import sys
sys.stdin=open('input.txt','r')

'''
3 2
1 5 3
8 3

둘다 내림차순 정렬
8 3 
5 3 1 

8 >=5 : cnt+=1, 그 다음으로 넘어감
3 >=3 : cnt+=1
끝



'''

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    bulk=sorted(list(map(int,input().split())),reverse=True)
    truck=sorted(list(map(int,input().split())),reverse=True)
    #print(bulk)
    ans=0
    s=0

    for i in range(s,M):
        for j in range(s,N):
            #print(i,j)
            if truck[i] >= bulk[j]:
                ans+=bulk[j]
                s+=1
                break
            s+=1
            # else:
            #     continue
    print('#{} {}'.format(tc,ans))
