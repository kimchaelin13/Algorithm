def fact(n): #f(n)=n*f(n-1)
    if n==1: #part1. basic
        return 1
    else: #part2. inductive(유도)
        return n*fact(n-1)

print(fact(4))