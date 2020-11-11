import sys
sys.stdin=open('input.txt','r')


alpha='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'

'''
3 ABC => AAABBBCCC

[A,B,C]이렇게 담아서 
한개씩 읽으면서 res+=A*3
'''

for tc in range(int(input())):
    res=''
    info=input().split()
    for i in info[1]:
       res += i*int(info[0])
    print(res)