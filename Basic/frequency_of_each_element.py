n = int(input())
d = {}

arr = []
for i in range(1,n+1):
    a = int(input())
    arr.append(a)
    d[a] = 0

for i in range(0,n):
    d[arr[i]] += 1 
for key,value in d.items():
    print(key,value)









