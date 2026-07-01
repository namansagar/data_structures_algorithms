n = int(input())
mat = []

for l in range(n):
    lst = []
    for m in range(n):
        lst.append(0)
    mat.append(lst)    
        
count = n

for i in range(n+1//2):
    for j in range(i, n-i):
        mat[i][j] = count
    for j in range(i, n-i):
        mat[n-1-i][j] = count
    for j in range(i, n-i):
        mat[j][i] = count
    for j in range(i, n-i):
        mat[j][n-1-i] = count
    count -= 1
    
for row in range(n):
    for column in range(n):
        print(mat[row][column], end = '')
    print()
