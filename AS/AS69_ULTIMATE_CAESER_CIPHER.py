import string

ciph = int(input("Shift key: "))

alphabet=string.ascii_lowercase

with open("cipher.txt","r") as ef:
    for line in ef:
        text=line.strip("\n")
        mess=''
        for i in text:
            if i==' ':
                mess=mess+i
            else:
                index=alphabet.rfind(i)
                p=index+ciph
                if p>26:
                    p=p-26
                mess = mess+alphabet[p]
                
        print(mess)
