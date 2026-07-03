n = int(input())

def counting(x):
    if x == 0:
        return
    print(x)
    counting(x-1)

counting(n)