import sys
sys.stdin=open('input.txt','r')



'''
합이 0이 되는 부분수열의 모든 경우의 수를 구해야한다(cnt)
전체수열을 처음부터 읽어주면서
더해준다. 만약에 
'''

def f(idx,d):
    global res

    if idx>=n:
        if s==d:
            res+=1
            return
    else:
        f(idx+1,d+arr[idx])
        f(idx+1,d)

if __name__=='__main__':
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    res=0
    f(0,0)
    if(s):
        print(res)
    else:
        print(-1)