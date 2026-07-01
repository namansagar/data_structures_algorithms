n = 1
pat = ''
for i in range(1,6):
    n = str(n)
    pat = n * i
    print(pat)
    n = int(n)
    n += 1