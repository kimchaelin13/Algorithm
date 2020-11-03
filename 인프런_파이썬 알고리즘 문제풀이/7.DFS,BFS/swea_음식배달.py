
import sys
sys.stdin=open('input.txt','r')



for tc in range(1,int(input())):
    n=int(input())
    maze=[list(map(int,input().split())) for _ in range(n)]
    hs=[]
    rs=[]
    cb=[0]
