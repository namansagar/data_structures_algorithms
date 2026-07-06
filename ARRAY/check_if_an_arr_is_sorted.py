arr = [5,4,6,7,8]
n = 5
count = True
for i in range(n-1):
    j = i + 1
    if(arr[i] <= arr[j]):
        j += 1
    else:
        count = False
print(count)