import sys
sys.stdin=open('input.txt','r')

'''
6 4
4 1
8

#1.입력을 먼저 받는다
#2.x,y따로 생각해야함

x 4 5 6 5 4 3 2 1 0 1 2 3 4 5 6 ...
y 1 2 3 4 3 2 1 0 1 2 3 ...

x 
[0,1,2,3,4,5,6,5,4,3,2,1]
y [0,1,2,3,4,3,2,1]

'''

w,h=map(int,input().split())
x,y=map(int,input().split())
t=int(input())

r_x = [i for i in range(w)] + [j for j in range(w,0,-1)]
r_y= [i for i in range(h)] + [j for j in range(h,0,-1)]

t_x,t_y=r_x.index(x),r_y.index(y)
res_x = r_x[(t_x + t)%len(r_x)]
res_y= r_y[(t_y +t )%len(r_y)]
print(res_x, res_y)