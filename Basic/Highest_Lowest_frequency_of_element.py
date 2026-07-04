n = int(input())
d = {}

arr = []
for i in range(1,n+1):
    a = int(input())
    arr.append(a)
    d[a] = 0

for i in range(0,n):
    d[arr[i]] += 1 
high = arr[0]
low = arr[0]

for i in range(0,n):
    if(d[arr[i]] > d[high] ):
        high = arr[i]
    if(d[arr[i]] < d[low]):
        low = arr[i]


print(high,low)
