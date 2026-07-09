arr = [1,1,0,0,0,2,1,2,2,0,1]
idx = -1
for j in range(len(arr)):
    if(arr[j] == 0):
        idx += 1
        arr[j],arr[idx] = arr[idx],arr[j]     
for k in range(len(arr)):
    if(arr[k] == 1):
        idx += 1
        arr[k],arr[idx] = arr[idx],arr[k]     
print(arr)
