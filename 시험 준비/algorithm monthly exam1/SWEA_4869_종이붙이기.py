import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N=int(input())
    lists=[]
    lists.append(1)
    lists.append(3)
    for i in range(2,N//10):
        lists.append(lists[i-1] + (lists[i-2])*2)
    print('#{} {}'.format(tc,lists.pop()))
