import sys
sys.stdin = open("input.txt", "r")

'''
12-45-78


'''
N=int(input())
result=''
for i in range(len(N)):
    str_N=str(N)
    temp=''

    for i in range(len(str_N)):
        if i == '3' or i=='6' or i=='9':
            temp+='-'

    if len(temp)==0:
        result+=i
    else:
        result+=temp
print(result+temp)