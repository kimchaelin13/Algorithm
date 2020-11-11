import sys
sys.stdin=open('input.txt','r')



def check(S):
    total=0
    S.insert(len(S),0)
    ch=[0]*26
    s=1
    for i in range(s,len(S)):
        if S[s-1] != S[s]:
            ch[(ord(S[s-1])-97)] +=1
            if ch[(ord(S[s-1])-97)] > 1:
                return False
        s+=1
    total+=1
    return True

W=[]
N=int(input())
for _ in range(N):
    W.append(list(input()))
ans=0
for i in range(N):
    ans += check(W[i])
print(ans)





# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)
#
