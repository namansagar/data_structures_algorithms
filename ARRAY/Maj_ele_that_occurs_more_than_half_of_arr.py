arr = [7,0,0,1,7,7,2,7,7]
n = len(arr)
d = {}
flag = False
for i in range(len(arr)):
    d[arr[i]] = 0

for j in range(len(arr)):
    d[arr[j]] += 1
    if(d[arr[j]] > int(n/2) ):
        flag = True
        print(arr[j])
        break

# METHOD 2:- 
# Boyer Moore Majority vote Algorithm
arr = [7,0,0,1,7,7,2,7,7]
count = 0
ans = 0
for i in range(len(arr)):
    if(count == 0):
        ans = arr[i]
        count = 1
    elif(arr[i] == ans):
        count += 1
    else:
        count -= 1
print(ans)
