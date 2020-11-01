arr=[1,2,3]

N=3

#sel안만들고, arr의 위치를 변경하면서 순열을 바꾸는것
def perm(idx):

    if idx==N:
        print(arr)
        return

    for i in range(idx,N):
        arr[idx],arr[i]=arr[i],arr[idx]
        perm(idx+1)
        arr[idx],arr[i]=arr[i],arr[idx]

perm(0)