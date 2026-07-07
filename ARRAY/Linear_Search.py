arr = [1,2,3,4,5]
n = 5
result = False
num = int(input())
for i in range(0,n):
    if(arr[i] == num):
        result = True
        print(i)
if(result == False):
    print(-1)