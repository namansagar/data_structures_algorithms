arr = [1 ,2 ,4 ,7 ,7 , 5]
n = 6

largest = 0
result = 0

if(len(arr) == 1):
    print("second largest = -1")
    print("second smallest = = -1")

for i in range(n):
    if(arr[i] > largest):
        largest = arr[i]
for j in range(n):
    if(arr[j] < largest and arr[j] > result):
        result = arr[j]
    if(arr[j] == largest):
        continue
print(result)

smallest = 0
b = arr[0]
for i in range(1,n):
    if(b >= arr[i] ):
        b = arr[i]

answer = 10 ** 5
for i in range(n):
    if (arr[i] > b):
        answer = min(answer, arr[i])
print(answer)