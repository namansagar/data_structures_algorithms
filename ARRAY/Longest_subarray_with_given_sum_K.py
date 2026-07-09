arr = [10,5,2,7,1,9]
k = int(input())
sum = 0
ans = 0
st = 0
end = 0
for end in range(len(arr)):
    sum += arr[end]
    if(sum > k):
        sum -= arr[st]
        st += 1
    if(sum == k):
        ans = max(ans,end - st + 1)
print(ans)