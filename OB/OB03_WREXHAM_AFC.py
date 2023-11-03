import random
text=[]

class wrexham:
    def __init__(self):
        self.__playernumber=""
        self.__forename=""
        self.__surname=""
        self.__position=""
        self.__communityinvolvement=0
        self.__injured=0
    def constructor(self, playernumber, forename, surname, position):
        self.__playernumber=playernumber
        self.__forename=forename
        self.__surname=surname
        self.__position=position
        self.__communityinvolvement=0
        self.__injured=False
    def getplayerinfo(self):
        return self.__forename, self.__surname, self.__position
    def changecommunityinvolvement(self, communityinvolvement):
        self.__communityinvolvement=communityinvolvement
    def changeinjured(self,injured):
        self.__injured=injured
    

with open("wrexham.txt","r") as ef:
    for line in ef:
        text.append(line.strip("\n"))

team=[]
for i in range(0,len(text),4):
    u=wrexham()
    u.constructor(text[i],text[i+1],text[i+2],text[i+3])
    team.append(u)


i = random.randint(1,28)
print(team[i].getplayerinfo())
team[i].changecommunityinvolvement(2)
team[i].changeinjured(True)
