import sys
sys.stdin=open('input.txt','r')

#
# S = input()
#
# ans = ''
# for i in S:
#     if ord(i) + 13 > 109:
#         ans += chr((ord(i) + 13) - 26)
#     else:
#         ans += chr(ord(i)+13)
# print(ans)

up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
down = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

s=  input()
ans = ''
for i in s:
    if i in up:
        ans += up[(up.index(i) + 13)%26]
    elif i in down:
        ans += down[(down.index(i) + 13)%26]
    else:
        ans += i
print(ans)