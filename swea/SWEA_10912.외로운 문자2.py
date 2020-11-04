import sys
sys.stdin=open('input.txt','r')

s='aaaba'

'''
#1.
s의 길이 만큼 돌면서 
스택이 비어있으면 s[i]를 넣는다.
        아니라면, 가장 위에 있는것과 지금 거를 비교한다. 그리고 두개가 같으면 => 위에있는걸 pop한다
                                                            다르면 => 지금거를 위에 push한다
                                                            
#2.마지막에 stack에 있는걸 출력한다



def check(s):
    stack=[]
    for i in range(N):
        pi=s[i]
        if len(stack)==0:
            stack.append(pi)
        else:
            if stack[-1] == pi:
                stack.pop(-1)
            else:
                stack.append(pi)
    if len(stack)==0:
        return 'Good'
    return stack
for tc in range(1,int(input())+1):
    s=input()
    s=sorted(s)
    N=len(s)
    result=''.join(check(s))
    print('#{} {}'.format(tc,result))

'''

for tc in range(1,int(input())+1):
    line=list(input())

    for i in range(len(line)):
        if line[i] != 'A':
            for j in range(i+1,len(line)):
                if line[i]==line[j]:
                    line[i]=line[j]='A'
                    break
    line=sorted(line)
    line=line[line.count('A'):]

    if line:
        print('#{} {}'.format(tc,''.join(line)))
    else:
        print('#{} Good'.format(tc))


