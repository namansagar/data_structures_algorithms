s = input()

def Palindrome(x,i,j):
    if i == j:
        return True
    if(x[i] == x[j]):
       return Palindrome(x,i+1,j-1)
    if(x[i] != x[j]):
        return False
        
flag = Palindrome(s,0,len(s)-1)
if (flag == True):
    print("palindrome")
if(flag == False):
    print("Not Palindrome")