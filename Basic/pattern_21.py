n = int(input())
for i in range(1,n+1):
    pat = ""
    if(i > 1 and i < n):
        pat = pat + "*"
        pat = pat + " "*(n-2)
        pat = pat + "*"
        print(pat)
    else :
        pat = pat + "*"*n
        print(pat)

