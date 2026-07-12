nums = [100, 4, 200, 1, 3, 2]
max_len = 0
nums = set(nums)
for num in nums:

    if num - 1 not in nums:
        current = num
        length = 1

        while current + 1 in nums:
            current += 1
            length += 1

        max_len = max(max_len, length)

print(max_len)