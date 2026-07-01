n = int(input())

for i in range(1,n+1):
   count = n - i
   a = 65
   pat = ""
   for j in range(1,i+1):
      pat = pat + chr(a)
      a += 1
   a -= 2
   for k in range(1,i):
      pat = pat + chr(a)
      a -= 1
   print(" " * count + pat)
   count -= 1


