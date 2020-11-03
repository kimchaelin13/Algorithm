'''
재귀로 1,2,3을 출력해야지
'''

def DFS(x):
    if x<4:
        print(x,end=" ")
        DFS(x+1)


if __name__=="__main__":
    n=int(input()) #n=1
    DFS(n)