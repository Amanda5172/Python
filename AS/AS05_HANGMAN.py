wordlist = ['word','shark','lightning','thief']

import random

r = random.randint(1,len(wordlist)-1)

word = wordlist[r]
let=[] #correct letters in word guessed
lette=[] #all letters guessed

for i in word:
    print('_ ', end='')

print()
t=False

count = 10

while t==False and count!=0:
    print()
    le = input("Guess a letter: ")

    t=True
    
    if le == word:
        t=True
    elif len(le) == 1:
        if le in lette:
            print("You have already guessed this letter.")
            t=False
        elif le in word:
            let.append(le)
            for p in word:
                if p in let:
                    print(p, end='')
                else:
                    print('_ ',end='')
                    t=False
        else:
            count=count - 1
            print(count,"strikes left.")
            t=False
            for p in word:
                if p in let:
                    print(p, end='')
                else:
                    print('_ ',end='')
                    t=False
            print()
    else:
        t=False
    lette.append(le)
    
print()

if t==True:
    print("You win!")
if count==0:
    print("You lose!")
    print("The word was",word)


    
