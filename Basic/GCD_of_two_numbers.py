N_1 = int(input())
N_2 = int(input())
gcd = 1

small = N_1 if N_1 < N_2 else N_2
for i in range(1,small+1):
    if(N_1 % i == 0 and N_2 % i == 0):
        gcd = i
print(gcd)