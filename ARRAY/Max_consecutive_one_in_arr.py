arr = [1,0,1,1,0,1]
result = 0
count = 0
for i in arr:
    if(i == 1):
        count += 1
        result = max(result, count)
        
    else:
        count = 0
print(result)