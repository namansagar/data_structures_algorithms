arr = [12, 31, 35, 8, 32, 17]    # TC : Average/practical : O(nlogn)  , SC : O(1) we did'nt took any extra space.
n = 6                            # TC : worst case: O(n^2) when pivot : smallest or largest in arr.

def partition(arr, st, end):
    idx = st - 1
    pivot = arr[end]

    for j in range(st, end):
        if(arr[j] <= pivot):
            idx += 1
            arr[j],arr[idx] = arr[idx],arr[j]
    idx += 1
    arr[end],arr[idx] = arr[idx],arr[end]
    return idx


def quick_Sort(arr, st, end):
    if(st < end):
        pivIdx = partition(arr, st, end)

        quick_Sort(arr, st, pivIdx - 1) # left half
        quick_Sort(arr, pivIdx + 1, end) # right half

quick_Sort(arr, 0, len(arr) - 1)

for i in arr:
    print(i,end = " ")