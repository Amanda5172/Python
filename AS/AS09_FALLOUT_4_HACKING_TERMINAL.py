import random

word=[]
display=[]

#used a text file for 5 letter words
with open("sgb-words.txt","r") as ef:
    for line in ef:
        word.append(line.strip())
        
for i in range(5):
    r = random.randint(0,len(word)-1)
    display.append(word[r])

print("Your words:",*display)
r = random.randint(0,4)
chosen = display[r]
user=""
count=0

while count<4 and chosen!=user:
    like=0
    letters=[]
    user = input("Guess: ")
    if chosen ==user:
        print("Correct!")
        break
    else:
        for i in user:
            if i in chosen and i not in letters:
                like = like+1
            letters.append(i)
    print("Likeness:",like)
    count=count+1

if count == 4:
    print()
    print("You have been locked out.")
    print(f"The word was {chosen}.")
            
