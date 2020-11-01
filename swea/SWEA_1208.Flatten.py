import sys
sys.stdin=open('input.txt','r')

'''
834
42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 

#1.입력받고, 숫자는 리스트로 받음
#2.일단 sort써서 오름차순정렬한다.
#3.834만큼 돌면서, 각 회차마다 맨 마지막은 -1, 맨 첫번째는 +1, 이거하고 나면 또 정렬함
#4.그리고 다 돌고 나면, 맨 마지막과 맨 처음의 값을 빼서 답을 구한다
'''

for tc in range(1,11):
    N=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    s=1
    while s<=N:
        nums[-1]=nums[-1]-1
        nums[0]=nums[0]+1
        nums.sort()
        s+=1
    print('#{} {}'.format(tc,nums[-1]-nums[0]))