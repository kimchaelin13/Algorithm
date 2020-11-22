import sys
sys.stdin = open('input.txt','r')


# alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# ans = [0]*26
#
# s=input()
#
# for i in s:
#     n = alpha.index(i)
#     ans[n]+=1
# print(*ans)

a=[0]*26
for x in input():
    a[ord(x)-97]+=1
print(*a)

print(ord('A'))
print(ord('z'))