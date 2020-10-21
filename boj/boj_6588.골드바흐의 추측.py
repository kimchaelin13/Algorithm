import sys
sys.stdin=open('input.txt','r')

'''
입력=8
8보다 작은 수 중에 소수인 리스트를 뽑음(2제외)
그리고 random.sample 써서, l=random2개/
만약에 n되면, 
break하고 거기 담긴 리스트 => sorted해야
'''

n=int(input())

#소수 리스트 생성
sosu=[]
for i in range(3,n):
    if n % i == 0:
        continue
    else:
        sosu.append(i)
print(sosu)