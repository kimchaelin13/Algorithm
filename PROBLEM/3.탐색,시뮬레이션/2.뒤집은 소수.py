import sys
sys.stdin=open('input.txt')

def reverse(s):
    global tmp
    for j in s[::-1]:
        tmp+=j
    reversed.append(tmp)

if __name__=='__main__':
    n=int(input())
    nums=list(input().split())
    reversed=[]
    tmp=''
    for i in range(n):
        reverse(i)