arr = [-1,0,3,6]
n = 4
idx = 0
for j in range(idx + 1,n):
    arr[j],arr[idx] = arr[idx],arr[j]
    idx += 1
print(arr)

