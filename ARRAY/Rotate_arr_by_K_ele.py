arr = [1,2,3,4,5,6,7]
n = 7
k = int(input())
s = input()

if(s == "left"):
    for i in range(1,k + 1):  #for left rotate
        idx = 0
        for j in range(1,n):
            arr[j],arr[idx] = arr[idx],arr[j]
            idx += 1

if(s == "right"):
    for i in range(1,k + 1):
        idx = len(arr) - 1
        while(idx >= 1):
            j = idx - 1
            arr[j],arr[idx] = arr[idx],arr[j]
            idx -= 1

if( s == "left"):
    print(arr)
if(s == "right"):
    print(arr)