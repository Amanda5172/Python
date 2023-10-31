import string


text = input("Message: ")
ciph = int(input("Shift key: "))

alphabet=string.ascii_lowercase


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
