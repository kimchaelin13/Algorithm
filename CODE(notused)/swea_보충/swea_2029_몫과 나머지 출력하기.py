import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    a,b = map(int,input().split())
    sh = a//b
    re = a%b
    print('#{} {} {}'.format(tc,sh,re))