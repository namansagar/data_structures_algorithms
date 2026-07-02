n = input()
s = 0
for i in range(len(n)):
    s = s + int(n[i]) ** len(n)

if (s == int(n)):
    print("True")
else:
    print("False")