import sys
sys.stdin=open('input.txt','r')

'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10


#1. 만약에 가장 큰 숫자가 첫자리에 없다면? 첫자리의 숫자 <-> 가장 큰 숫자 

#2. 가장 큰 숫자가 여러개라면? 가장 뒤에 있는 숫자와 체인지


123 1 => 가장 큰 숫자와 맨앞자리와 바꾼다. (가장 큰 숫자가 맨앞에 있다면? 그 다음 큰 숫자와 두번째를 바꾼다)
2237 1 => 


'''



# for tc in range(1,int(input())+1):

#5c2
arr=[3,2,8,8,8]
N=len(arr) ; cnt=2#원하는 교환횟수
ans=0
visit=[set() for _ in range(11)]

def backtrack(k):
    global ans
    num = int(''.join(map(str, arr)))
    if num in visit[k]: return
    else:
        visit[k].add(num) #일종의 방문체크

    if k==cnt:
        if ans<num:
            ans=num; #print(ans)

    else:
        for i in range(N-1):
            for j in range(i+1,N):
                arr[i],arr[j]=arr[j],arr[i]
                backtrack(k+1)
                arr[i],arr[j]=arr[j],arr[i]
backtrack(0)
print(ans)