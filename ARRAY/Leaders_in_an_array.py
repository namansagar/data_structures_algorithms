arr = [10,22,12,3,0,6]
leader = []
max = arr[len(arr) - 1]
leader.append(max)

for i in range(len(arr) - 2,-1,-1):
    if(arr[i] > max):
        max = arr[i]
        leader.append(max)

leader.reverse()
print(leader)