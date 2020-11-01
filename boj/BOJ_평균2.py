import sys
sys.stdin = open("input.txt", "r")

N=int(input())
grades=list(map(int,input().split()))
max_grade=max(grades)

for i in range(N):
    grades[i]=(grades[i]/max_grade)*100

avg=sum(grades)/N
print(avg)