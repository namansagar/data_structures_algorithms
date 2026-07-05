arr = [12, 31, 35, 8, 32, 17]   # MERGE_SORT : TC = (total recursive calls) * (work done in each call) = O(nlogn) 
n = 6                                        # SC = O(n) -> because we consider the space of temp arr.

def merge(arr, st, mid, end):  # time complexity of merge step : O(n) , where n = total no. of ele in the arr.
    temp = []
    i = st
    j = mid + 1
    
    while(i <= mid and j <= end):
        if(arr[i] <= arr[j]):       # for sorting descending order if make the sign opposite it will sort it dec order.
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while(i <= mid):
        temp.append(arr[i])    #if left half elements are left
        i += 1
    
    while(j <= end):
        temp.append(arr[j])    # if right half elements are left
        j += 1
    
    for idx in range(0,len(temp)):
        arr[idx + st] = temp[idx]


def merge_sort(arr, st, end):
    if(st < end):
        mid = int(st + (end - st)/2)

        merge_sort(arr, st, mid) # for left half
        merge_sort(arr, mid + 1, end) #for right half

        merge(arr, st, mid, end)

merge_sort(arr, 0,len(arr)-1)
                      #|-> end is the last idx of arr not the len of arr
for i in arr:
    print(i,end = " ")