import sys
sys.stdin=open('input.txt','r')

h=[]
flag=0
for _ in range(9):
    h.append(int(input()))
h.sort()
for a in range(3):
    for b in range(a+1,4):
        for c in range(b+1,5):
            for d in range(c+1,6):
                for e in range(d+1,7):
                    for f in range(e+1,8):
                        for g in range(f+1,9):
                            if h[a]+h[b]+h[c]+h[d]+h[e]+h[f]+h[g] == 100:
                                print(h[a],h[b],h[c],h[d],h[e],h[f],h[g],sep='\n')
                                flag=1
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break

# h.sort()
# total = sum(h)
# flag=0
# for i in range(8):
#     for j in range(i+1,9):
#         if total - h[i] - h[j] == 100:
#             for k in range(9):
#                 if k!=i and k!=j:
#                     print(h[k])
#             flag=1
#             break
#     if flag:
#         break