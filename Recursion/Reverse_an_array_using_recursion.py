N = int(input())
arr = []

for i in range(N):
    x = int(input())
    arr.append(x)
    
lst = []

def Reverse(n, array):
    if n == 0:
        return
    lst.append(array[n-1])
    Reverse(n-1, array)
    return lst

print(Reverse(N, arr))