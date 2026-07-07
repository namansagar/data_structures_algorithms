arr_1 = [1,2,3,4,5,6,7,8,9,10]
n = 10
arr_2 = [2,3,4,4,5,11,12]
m = 7
union = []
j = 0
idx = 0
for i in range(0,n):
    if(arr_1[idx] <= arr_2[j]):
        union.append(arr_1[i])
        idx += 1
    else:
        union.append(arr_2[j])
        j += 1

while(idx <= n-1):
    union.append(arr_1[idx])
    idx += 1
while(j <= m-1):
    union.append(arr_2[j])
    j += 1

print(list(set(union)))

