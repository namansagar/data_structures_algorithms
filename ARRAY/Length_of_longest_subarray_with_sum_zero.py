arr = [9, -3, 3, -1, 6, -5]
k = 0
st = 0
end = 0
sum = 0
ans = 0
for end in range(len(arr)):
    sum += arr[end]
    if(sum > k):
        sum -= arr[st]
        st += 1
    if(sum == k):
        ans = max(ans,end - st + 1 )
print(ans)