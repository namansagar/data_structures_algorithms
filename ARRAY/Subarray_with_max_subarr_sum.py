arr = [2, 3, 5, -2, 7, -4]
curr_sum = 0
max_sum = float('-inf')
curr = []
max_sum_subarr = []

for val in arr:
    curr_sum += val
    curr.append(val)
    
    if curr_sum > max_sum:
        max_sum = curr_sum
        max_sum_subarr = curr.copy()

    if(curr_sum < 0):
        curr_sum = 0
        curr.clear()

print(max_sum)
print(max_sum_subarr)