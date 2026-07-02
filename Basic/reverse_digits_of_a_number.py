num = input()
rev = num[::-1]
i = 0
for i in range(len(rev)):
        if(rev[i] != '0'):
            break
rev = rev[i:]
print(rev)

