import random
text=[]

class cat:
    def __init__(self):
        self.__name=""
        self.__description=""
        self.__weight=""
        self.__length=""
        self.__lifeexpectancy=""
        self.__imageurl=""
    def constructor(self, name, description, weight, length, life, imageurl):
        self.__name=name
        self.__description=description
        self.__weight=weight
        self.__length=length
        self.__lifeexpectancy=life
        self.__imageurl=imageurl
    def getcatdetails(self):
        return self.__name, self.__description, self.__weight, self.__length, self.__lifeexpectancy, self.__imageurl
    def getcatlife(self):
        return self.__name, self.__lifeexpectancy
    

with open("CutestCats.txt","r") as ef:
    for line in ef:
        if line!="\n":
            text.append(line.strip("\n"))



cats=[]
for i in range(0,len(text),7):
    u=cat()
    u.constructor(text[i],text[i+1],text[i+2],text[i+3],text[i+5],text[i+6])
    cats.append(u)


i = random.randint(0,4)
print(cats[i].getcatdetails())
print(cats[i].getcatlife())
