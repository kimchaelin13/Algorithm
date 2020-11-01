def fibo2(n):
    global memo #이거 왜있는지 잘 모르겠닷
    if n >=2 and len(memo) <= n:
        memo.append(fibo2(n-2)+fibo2(n-1))
    return memo[n]



memo=[0,1] #참조형(read and write),
#ans = 0 #값형
print(fibo2(7))