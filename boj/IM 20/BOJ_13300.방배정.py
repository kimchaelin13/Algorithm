import sys
sys.stdin=open('input.txt','r')


'''
16 2
1 1
0 1
1 1
0 2
1 2
0 2
0 3
1 3
1 4
1 3
1 3
0 6
1 5
0 5
1 5
1 6

'''
N,M=map(int,input().split())

rooms_m = [0]*7
rooms_f = [0]*7
cnt = 0
for _ in range(N):
    gender, grade = map(int,input().split())
    #여지일경우
    if gender == 0:
        rooms_f[grade] +=1
        if rooms_f[grade] > M:
            cnt+=1
            rooms_f[grade]=rooms_f[grade] - M
    else:
        rooms_m[grade] +=1
        if rooms_m[grade] > M:
            cnt +=1
            rooms_m[grade] = rooms_m[grade]-M

#답 구하기
for f in rooms_f:
    if f!=0:
        cnt +=1
for m in rooms_m:
    if m!=0:
        cnt +=1
print(cnt)