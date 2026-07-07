arr = [2,3,4,5,9,8,7,6]
arr.sort()
for i in range(1,len(arr)+1):
    if(arr[i-1] != i):
        break
print(i)