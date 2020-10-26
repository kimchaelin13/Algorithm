import sys
sys.stdin = open("input.txt", "r")


'''
리스트로 입력을 받고, 
RESULT리스트를 만들어서 원리스트를 돌면서 42로 나눈 나머지를 넣어준다
'''

result=[]
for _ in range(10):
    N=int(input())
    if N%42 not in result:
        result.append(N%42)
print(len(result))