x = int(input())

def Sum_of_N(n):

    if n == 0:
        return 0
    return n + Sum_of_N(n-1)

print(Sum_of_N(x))

