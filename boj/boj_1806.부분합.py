import sys
sys.stdin=open('input.txt','r')

'''
10 15
5 1 3 5 10 7 4 9 2 8
투포인터 문제

SOLUTION
위 문제는 투포인터 알고리즘으로 풀이하면 쉽게 풀린다.

알고리즘은 어렵지 않다.

말그대로 start 포인터와 end 포인터를 활용해 start~end 까지의 합을 구해주는 방식이다.

end는 항상 start를 초과하고 두 포인터 모두 증가하는 방향으로 나아간다.

 

1) 주어진 리스트의 sum_A리스트를 따로 하나 생성한다. (첫항부터 자신 까지의 합이 담긴 리스트)

2) start = 0, end = 1로 놓는다.

3) sum_A[end] - Sum_A[start]를 기반으로 다음 if문을 실행한다.

 

4-0) (start, end)가 (n-1, n)이 되면 종료한다.

4-1) sum_A[end] - sum_A[start] 가 S이상일 경우 answer에 길이를 담아준다. 이후 start에 +1 해주어 다음으로 넘어간다.

4-2) sum_A[end] - sum_A[start] 가 S미만일 경우 end에 +1 해주어 다음으로 넘어간다.

4-3) end가 마지막에 도달했을 경우 start에 +1해준다.
'''

N,S=map(int,input().split())
nums=list(map(int,input().split()))

sum_nums=[0]*(N+1)
for i in range(1,N+1):
    sum_nums[i]=sum_nums[i-1]+ nums[i-1]

answer=987654321
flag=1
start=0
end=1

while start!=N:
    if sum_nums[end]-sum_nums[start] >=S:
        if end-start<answer:
            answer=end-start
            flag=0
        start+=1
    else:
        if end!=N:
            end+=1
        else:
            start+=1

if flag != 1:
    print(answer)
else:
    print(0)