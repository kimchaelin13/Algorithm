############################################################
#2차원 배열 90도 회전

def rotate_90(m):
    N=len(m)
    ret=[[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_90(test))

############################################################

#2차원 배열 180도 회전

def rotate_180(m):
    N=len(m)
    ret=[[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret
print(rotate_180(test))


###############################################################

#270도 회전

def rotate_270(m):
    N=len(m)
    ret=[[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r]=m[r][c]
    return ret
test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_270(test))


################################################################

#최종 함수

# 이제 위의 함수들을 모아 사용자 원하는 만큼 회전하는 알고리즘을 작성하자.이 함수는 원 배열 m과 함께 몇 도 회전할지에 대한 입력도 받아야 한다
#
# 그 입력을 90도 단위로 하는 d로 받자. 90도는 1, 180도는 2, 270도는 3,,

def rotate(m,d):
    N=len(m)
    ret=[[0]*N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N - 1 - r] = m[r][c]
    elif d % 4 ==2:
        for r in range(N):
            for c in range(N):
                ret[N - 1 - c][N - 1 - r] = m[r][c]
    elif d % 4 ==3:
        for r in range(N):
            for c in range(N):
                ret[N - 1 - c][r] = m[r][c]

    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret
