n = int(input())  
s = 0  
i = n                     
while(i > 0):
    count = int(i/2)
    pat = ""
    for m in range(1,count+1):
        pat = pat + "*"

    pat = pat + " "*s
    s += 2

    for k in range(1,count+1):
        pat = pat + "*"
    print(pat)
    i -= 2

d = 8
j = 2
while(j <= n):
    count = int(j/2)
    pat = ""
    for m in range(1,count+1):
        pat = pat + "*"

    pat = pat + " "*d
    d -= 2

    for k in range(1,count+1):
        pat = pat + "*"
    print(pat)
    j += 2


 

