import random
text=[]

class joke:
    def __init__(self):
        self.__prompt=""
        self.__answer=""
    def constructor(self, prompt, answer):
        self.__prompt=prompt
        self.__answer=answer
    def getprompt(self):
        return self.__prompt
    def getanswer(self):
        return self.__answer
    

with open("DadJokes.txt","r") as ef:
    for line in ef:
        text.append(line.strip("\n"))

jokes=[]
for i in range(0,len(text),2):
    u=joke()
    u.constructor(text[i],text[i+1])
    jokes.append(u)


i = random.randint(0,9)
print(jokes[i].getprompt())
userans=input()
print(jokes[i].getanswer())
