import sys
sys.stdin=open('input.txt','r')



n=int(input())
meeting=[]
for _ in range(n):
    s,e=map(int,input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x:(x[1],x[0]))

cnt=0
et=0
for s,e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)








# n=int(input())
# meeting=[]
# for _ in range(n):
#     s,e=map(int,input().split())
#     meeting.append((s,e))
# #우선순위가 x[1]로 소트하겠다는 뜻이다.원래 기본값으로 정렬하면
# meeting.sort(key=lambda x: (x[1],x[0]))
#
# et=0
# cnt=0
# for s,e in meeting:
#     if s>=et:
#         et=e
#         cnt+=1
# print(cnt)
