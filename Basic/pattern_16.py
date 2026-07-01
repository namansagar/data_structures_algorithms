count = 5
a = 65
for i in range(1,6):
    pat = ""
    for j in range(1,i+1):
        pat = pat + chr(a)
        
    print(pat)
    count -= 1
    a += 1

