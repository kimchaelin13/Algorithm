arr = [1, 2, 3, 4]
N = 4
R = 2

sel = [0] * R


# 셀의 idx와 배열의 idx를 컨트롤할것
def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i + 1, sidx + 1)


combination(0, 0)



def combination2(idx,sidx):
    if sidx==R:
        print(sel)
        return

    if idx==N:
        return
    sel[idx]=arr[idx]
    #뽑고 가고
    combination2(idx+1,sidx+1)
    #안뽑고가고
    combination2(idx+1,sidx)

combination2(0,0)