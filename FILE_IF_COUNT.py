cif=0
cmam=0

with open("if.txt","r") as ef:
    for line in ef:
        if " if " in line or "If " in line:
            cif = cif+1
            
with open("mam.txt","r") as ef:
    for line in ef:
        if " if " in line or "If " in line:
            cmam = cmam+1

with open("if.txt","a") as kf:
    kf.write(str(cif))
with open("mam.txt","a") as kf:
    kf.write(str(cmam))

if cif > cmam:
    print("The word 'if' appears more in 'if' than 'ma'am'")
elif cif < cmam:
    print("The word 'if' appears more in 'ma'am' than 'if'")

