arr = [4,1,5,2,3]
n = 5
#compare adjacent elements :4,1 then 1,5 ...
#push the largest element in the end of the array


def bubblesort(arr,n):    #O(n^2)
    for i in range(n-1):
        is_swap = False
        for j in range(n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_swap = True
            
                
    print(arr)
            
(bubblesort(arr,n))
            
# for descending order change the sign where comparision is happening 