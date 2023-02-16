CheckNum=input()
s=str(CheckNum)
n=0

for i in range(len(s)):
    if i< len(s)-1:
        m=len(s)-i
        b=int(s[i])*m
        n=n+b
        
mod = n%11
rem = 11-mod

if rem == 11:
    rem=0
elif rem == 10:
    rem= 'X'
    

if str(rem) == s[i]:
    print("Check passed.")
