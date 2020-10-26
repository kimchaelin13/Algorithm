import sys
sys.stdin = open("input.txt", "r")

'''
*
**
***
****
*****
일단 큰 for문이 5번 돌아야 함
그리고 안 for문에서는? 

와 왜 2중 for문을 생각했지? 
그냥 하나다. 규칙이 단한개임. 
'''
n=int(input())
for i in range(1,n+1):
    print('*'*i)