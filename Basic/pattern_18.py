for i in range(1,6):
    a = 69
    pat = ''
    for j in range(1,i+1):
        pat = chr(a) + pat
        a -= 1
    print(pat)