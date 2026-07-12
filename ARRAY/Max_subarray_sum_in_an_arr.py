# KADANE's ALGORITHM :-  time complexity : O(n)

arr = [-1,-2,-3,-4,-5]
curr_sum = 0
max_sum = float('-inf')

for val in arr:
    curr_sum += val
    max_sum = max(curr_sum,max_sum)

    if(curr_sum < 0):
        curr_sum = 0
print(max_sum)