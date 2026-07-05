arr = [4,1,5,2,3]
n = 5

def selection_sort(arr,n):   # O(n^2)
    for i in range(0,n-1):
        smallest_Idx = i      #starting element of unsorted part
        for j in range(i+1,n):
            if(arr[j] < arr[smallest_Idx]):
                smallest_Idx = j
        arr[i],arr[smallest_Idx] = arr[smallest_Idx],arr[i]
    print(arr)

selection_sort(arr,n)


# for descending order change the sign where comparision is happening 

