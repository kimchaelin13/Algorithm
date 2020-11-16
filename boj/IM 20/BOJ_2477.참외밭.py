import sys
sys.stdin=open('input.txt','r')


N=int(input())

side_length=[]
for _ in range(6):
    d,l = map(int,input().split())
    side_length.append(l)

#1. find largest area / index
pos=0
largest_area = 0
for i in range(len(side_length)):
    if side_length[i-1]*side_length[i] > largest_area:
        largest_area = side_length[i-1] * side_length[i]
        pos = i-1
#1-1
# if side_length[0]*side_length[5] > largest_area:
#     largest_area = side_length[0] * side_length[5]
#     pos = 5

#2. find small one(clock-reverse => +3: hor , +4:ver)
h = (pos+3)%6
v = (pos+4)%6
# print(h,v)
smallest_area = side_length[h] * side_length[v]

#3. result area
final_area = largest_area - smallest_area

#4.number of fru
ans = N*final_area
print(ans)
