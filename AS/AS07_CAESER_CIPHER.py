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
        mess = mess+alphabet[index+ciph]
    

print(mess)
