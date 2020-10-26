import sys
sys.stdin = open("input.txt", "r")

'''
가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
'''

a,b = map(int,input().split())
if a==1 and b==3:
    print('A')
elif a==2 and b==1:
    print('A')
elif a==3 and b==2:
    print('A')
else:
    print('B')
