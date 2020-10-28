import sys
sys.stdin=open('input.txt','r')


'''
124783

3개 뽑아서 연속증가면 run+나머지가 모두 똑같으면 트리플렛 => 두개 다 있어야 베이비진 True

#1. 6개중에 임의로 3개를 뽑아서 3개짜리 조합을 만든다
#2. 그게 트리플렛인지 run인지 확인 
    -> 트리플렛이면, 나머지 카드가 run인지확인 => 맞으면 return True
    -> 런이면, 나머지 카드가 트리플렛인지 확인=> 맞으면 return True 
'''

def dfs(L,s):
    if L==len(res):
        for j in range(L):
            tmp.append(res[j])
        print()
    else:
        for i in range(s,len(cards)+1):
            res[L]=i
            dfs(L+1,i+1)

cards=list(map(int,input().split()))
#가능한 3개의 조합을 모두 뽑는다.
res=[0]*3
tmp=[]
dfs(0,cards[0])
print(tmp)

