N = 3

arr = [1, 2, 3]

sel = [0] * N

def powerset(idx):
    #도착을 했을때
    if idx == N:
        print(sel , " : ", end=" ")
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    #해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx+1)
    #해당자리를 안뽑고 가고
    sel[idx] = 0
    powerset(idx+1)


powerset(0)