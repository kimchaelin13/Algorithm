import sys
sys.stdin=open('input.txt','r')

'''
입략

5
5457
6 7 8
100
1 0 5
99999
0 2 3 4 5 6 7 8 9
158
1 9 2 5 4
151241
0 1 2 3 4 7 8 9
'''
def remote_control(cnt, current_page):
    global length, minn, page
    if len(current_page) != 0:
        if cnt + abs(int(current_page) - page) < minn:
            minn = cnt + abs(int(current_page) - page)
    if len(current_page) > length + 1:
        return
    for i in not_broken:
        remote_control(cnt + 1, current_page + i)

page = 151241
broken = [0, 1, 2, 3, 4, 7, 8, 9]
minn = abs(page - 100)
length = len(str(page))
not_broken = []
for i in range(10):
    if i not in broken:
        not_broken.append(str(i))

remote_control(0, '')
print(minn)




# def find_near(i):
#     global rough_target
#     s = 1
#
#     #7없어, 그럼 8? 6 있어? 이걸 동시에 함.
#     #만약 있으면, 멈추고, 그 있는 8이나 6을 rough_target에 갖다 붙이고, 스탑
#     while True:
#         if int(i)-s in work:
#             rough_target += str(int(i)-s)
#             return
#         elif int(i)+s in work:
#             rough_target += str(int(i)+s)
#             return
#         else:
#             s+=1
#
# def find_min():
#     MIN=0
#     #rough
#     temp_r = len(rough_target) + abs(int(rough_target) - target)
#     #max
#     temp_max = len(rough_max) + (int(rough_max)-target)
#     #min
#     temp_min = len(rough_min) + (target - int(rough_min))
#
#     MIN=min(temp_r,temp_max,temp_min,abs(100-target))
#     return MIN
#
# for tc in range(1,int(input())+1):
#     target=int(input())
#     broken=list(map(int,input().split()))
#     work=[i for i in range(10) if i not in broken]
#
#     #만들수있는 가장 비슷한 채널 숫자를 만든다
#     rough_target=''
#     for i in str(target):
#         if int(i) in work:
#             rough_target += i
#         else:
#             find_near(i)
#
#     #rough_max은 target채널이 rough_target와 차이가 많이 날 경우, 한자리수를 늘려서 -로 내려올때 더 최솟값일 경우 때문에 만듦
#     #rough_min은 위와 반대의 이유로,..
#     rough_max,rough_min = '',''
#     rough_max = rough_target + str(min(work))
#     rough_min += str(max(work)) * (len(str(target))-1)
#
#     print('#{} {}'.format(tc,find_min()))
#

