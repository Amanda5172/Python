CheckNum=int(input())
s=str(CheckNum)
n=0

for i in range(len(s)):
    if i< len(s)-1:
        m=len(s)-i
        b=int(s[i])*m
        n=n+b
        
mod = n%11
rem = 11-mod

if rem == int(s[i]):
    print("Check passed.")
