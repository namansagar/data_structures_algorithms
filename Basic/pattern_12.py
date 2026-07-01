n = 4

for k in range(1, n + 1):

    
    for i in range(1, k + 1):
        print(i, end="")


    x = 2 * (n - k)
    print(" " *x , end="")

    
    for j in range(k, 0, -1):
        print(j, end="")

    print()