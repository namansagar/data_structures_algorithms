n = int(input())

def counting(x):
    if x == 0:
        return
    counting(x-1)
    print(x)

counting(n)

