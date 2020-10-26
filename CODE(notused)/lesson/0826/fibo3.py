def fibo3(n):
    f = [0,1] #memoization table
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibo3(3))

