
import sys
sys.stdin = open('input.txt', 'r')
'''
n번만큼 돌면서 input()으로 들어온거를 리스트에 담는다
그다음에 리스트에있는걸 정렬하고, 하나씩 읽고,세로출력
'''

N=int(input())
li=[]
for i in range(N):
    li.append(int(input()))
sort_li=sorted(li)
for i in sort_li:
    print(i)