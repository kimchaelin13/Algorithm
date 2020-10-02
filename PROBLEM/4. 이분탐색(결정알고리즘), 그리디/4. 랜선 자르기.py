import sys
sys.stdin=open('input.txt','r')

def Count(len):
    cnt=0
    for x in line:
        cnt+=(x//len)
    return cnt


if __name__=='__main__':
    k,n=map(int,input().split())
    line=[]
    res=0
    largest=0 #가장 긴 랜선을 찾아야지
    for i in range(k):
        tmp=int(input())
        line.append(tmp)
        largest=max(largest,tmp) #기존의 값과 새로운 값을 비교해서 가장 큰 값을 구한다
    lt=1
    rt=largest
    #이분검색
    while lt<=rt:
        mid=(lt+rt)//2
        #답이 되는지 안되는지 판명해주는 카운트 함수!
        if Count(mid)>=n:
            res=mid
            lt=mid+1
        else:
            #더 큰쪽을 버려야 하니까
            rt=mid-1
    print(res)

