import sys
sys.stdin=open('input.txt','r')
'''
시간초과 ㅅㅂ! 
'''

def calc(pos, length):
    dir = (pos + t) // length
    idx = (pos + t) % length
    if dir % 2 == 0:
        return idx
    else:
        return length - idx


W, H = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

print(calc(p, W), calc(q, H))


def check(x,y):
    global flag
    while len(res)<= h and flag==1:
        a=b=1
        if 0<x<w and 0<y<h:
            x=x+a
            y=y+b
            res.append((x,y))
        else:
            flag=0
            x=x-1
            y=y+1
            res.append((x,y))

            while flag==0 and 0<x<w and 0<y<h:
                a = b = -1
                x = x + a
                y = y + a
                res.append((x,y))
            flag=1


if __name__=='__main__':
    w,h=list(map(int,input().split()))
    x,y=list(map(int,input().split()))
    h=int(input())
    flag=1
    res=[(x,y)]
    check(x,y)
    # print(res)
    print(*res[8])


