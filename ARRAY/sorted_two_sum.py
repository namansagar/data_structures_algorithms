arr = [1,2,3,4,5]
k = int(input())
sum = 0
st = 0 
flag = False
end = len(arr) - 1
for i in range(len(arr)):
    if(st < end):
        sum = arr[st] + arr[end]
        if(sum > k):
            end -= 1
        elif(sum < k):
            st += 1

        else:
            (sum == k)
            flag = True
            break
if(flag == True):
    print("YES")
else:
    print("NO")