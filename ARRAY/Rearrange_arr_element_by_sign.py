arr = [3,1,-2,-5,2,-4]
pos = []
neg = []
idx = 0
n = len(arr)

for i in range(0,len(arr)):
    if(arr[i] > 0):
        pos.append(arr[i])
    if(arr[i] < 0):
        neg.append(arr[i])

for j in range(0,int(n/2)):
    arr[idx] = pos[j]
    arr[idx + 1] = neg[j]
    idx += 2

print(arr)