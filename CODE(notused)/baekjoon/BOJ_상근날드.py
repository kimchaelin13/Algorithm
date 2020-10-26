import sys
sys.stdin = open("input.txt", "r")

tmp=[]
for _ in range(5):
    tmp.append(int(input()))

burgers=tmp[:3]
coke=tmp[3:]

prices=[]
for i in range(3):
    for j in range(2):
        set_price = burgers[i]+coke[j]-50
        prices.append(set_price)
print(min(prices))
