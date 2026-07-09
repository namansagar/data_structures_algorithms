arr = [1,2,3,4,5]
k = int(input())
d = {}
flag = False
for j in range(len(arr)):
    if(k - arr[j] in d):
        flag = True
        break
    else:
        d[arr[j]] = j
if(flag == True):
    print("YES")
else:
    print("NO")
