arr = [4,1,5,2,3]
n = 5

def insertion_sort(arr,n):     # O(n^2)
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        while(prev >= 0 and arr[prev] > curr):
            arr[prev + 1] = arr[prev]
            prev -= 1
        
        arr[prev+1] = curr   # placing the current element in its correct position.
    print(arr)

insertion_sort(arr,n)


#to sort it in descending order just change the sign of greater than to less than {FOR EACH TYPE OF SORTING: selection,insertion,bubble}