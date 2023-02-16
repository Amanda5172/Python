CheckNum=input("Input the first 12 digits of the ISBN: ")
s=str(CheckNum)
n=0
m=1
for i in range(len(s)):
    if i< len(s):
        if m%2==0:
            j=3
            b=int(s[i])*j
            m=m+1
        else:
            j=1
            b=int(s[i])*j
            m=m+1
        n=n+b
 
mod = n%10
if mod!=0:
    rem = 10-mod
    
print("Check digit:",rem)
