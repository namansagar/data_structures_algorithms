arr = [4,1,2,2,1,5]
temp = []

for i in arr:
    if(arr.count(i) == 1):
        temp.append(i)
for j in temp:
    print(j,end = ' ')
print()