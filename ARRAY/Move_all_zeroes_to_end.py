arr = [1,0,2,3,0,4,0,1]
n = 8
idx = -1
for j in range(0,n):
    if(arr[j] != 0):
        idx += 1
        arr[j],arr[idx] = arr[idx],arr[j]
print(arr)
