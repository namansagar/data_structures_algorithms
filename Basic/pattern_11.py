n = 1
pat = ""
for i in range(1,6):
    if(n % 2 != 0):
        pat = "1" + pat
        print(pat)
    else:
        pat = "0" + pat
        print(pat)
    n += 1