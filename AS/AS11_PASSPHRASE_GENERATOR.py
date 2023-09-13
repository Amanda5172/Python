import string
import random

length = random.randint(10,20)

list1 = [0,1,2,3,4,5,6,7,8,9,"!","#","$","%","&","'","*","+","-","/","=","?","^","_","`","{","|","}","~"]
for i in string.ascii_letters:
    list1.append(i)


for r in range(length):
    num = random.randint(1,len(list1))
    print(list1[num],end='')

