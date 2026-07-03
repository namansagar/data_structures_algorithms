n = int(input())

def Fibonacci(x):
    if (x == 0):
        return 0
    if (x == 1):
        return 1
    return Fibonacci(x-2) + Fibonacci(x-1)

for i in range(n+1):
    print(Fibonacci(i),end = " ")
print()