#ranking:
#1 High Card: Highest value card.
#2 One Pair: Two cards of the same value.
#3 Two Pairs: Two different pairs.
#4 Three of a Kind: Three cards of the same value.
#5 Straight: All cards are consecutive values.
#6 Flush: All cards of the same suit.
#7 Full House: Three of a kind and a pair.
#8 Four of a Kind: Four cards of the same value.
#9 Straight Flush: All cards are consecutive values of same suit.
#10 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

def samesuit(player):
    h=0
    c=0
    s=0
    d=0
    
    for i in player:
        match i[1]:
            case "H":
                h = h+1
            case "C":
                c=c+1
            case "S":
                s=s+1
            case "D":
                d=d+1
    if h==5 or c==5 or s==5 or d==5:
        return True
    else:
        return False
    
                
def numarr(player):
    j=[]
    for t in range(14):
        j.append(0)
    
    for i in player:
        match i[0]:
            
            case "2":
                j[1]=j[1]+1
            case "3":
                j[2]=j[2]+1
            case "4":
                j[3]=j[3]+1
            case "5":
                j[4]=j[4]+1
            case "6":
                j[5]=j[5]+1
            case "7":
                j[6]=j[6]+1
            case "8":
                j[7]=j[7]+1
            case "9":
                j[8]=j[8]+1
            case "T":
                j[9]=j[9]+1
            case "J":
                j[10]=j[10]+1 #J=11
            case "Q":
                j[11]=j[11]+1 #Q=12
            case "K":
                j[12]=j[12]+1 #K=13
            case "A":
                j[13]=j[13]+1
            case _:
                j[0]=j[0]+1
                
    return j


def sameval(j): 
    pairs=[]
    three=[]
    four=[]
    sama=[] #2d array containing all three cases
            
    for k in range(len(j)):
        if j[k]==2:
            pairs.append(k+1)
        elif j[k]==3:
            three.append(k+1)
        elif j[k]==4:
            four.append(k+1)

    sama.append(pairs)
    sama.append(three)
    sama.append(four)

    return sama

        
def consecval(j):
    try:
        k = j.index(1)
        if j[k+1]==1 and j[k+2]==1 and j[k+3]==1 and j[k+4]==1:
            return True
    except:
        return False


def royflush(j):
    if j[9]==1 and j[12]==1:
        return True
    else:
        return False


def highval(j):
    for i in range(len(j)):
        if j[i]>0:
            k=i+1
    return k


def check(player):
    j = numarr(player)
    suit = samesuit(player) #true or false
    sama = sameval(j) #2d array
    highest = highval(j)
    highmatch=0
    rank=1
    
    if len(sama[0])==1:
        rank=2
        highmatch=sama[0][0]
        
    elif len(sama[0])==2:
        rank=3
        highmatch=sama[0][1]

    if len(sama[1])==1 and rank==2:
        rank=7
        highmatch=sama[1][0]
        
    elif len(sama[1])==1:
        rank=4
        highmatch=sama[1][0]
        
    elif len(sama[2])==1:
        rank=8
        highmatch=sama[2][0]

    
    con = consecval(j)
        
    if con==True and suit==True:
        roy = royflush(j) 
        if roy == True:
            rank=10
        else:
            rank=9
    elif suit==True:
        rank=6
        
    elif con==True:
        rank=5
            
    
    r = list([rank,highest,highmatch])
    return r


def compare(p1,p2):
    hand1 = check(p1)
    hand2 = check(p2)

    if hand1[0]>hand2[0]:
        return 1
    elif hand1[0]<hand2[0]:
        return 2
    elif hand1[2]!=0:
        if hand1[2]>hand2[2]:
            return 1
        elif hand1[2]<hand2[2]:
            return 2
        
    if hand1[1]>hand2[1]:
        return 1
    elif hand1[1]<hand2[1]:
        return 2       
        


play1=0
play2=0
with open("poker.txt","r") as ef:
    for line in ef:
        p1=[]
        p2=[]
        p = list(line.split())
        p1 = p[:5]
        p2 = p[5:]
        winner = compare(p1,p2)
        if winner==1:
            play1 = play1+1
        elif winner==2:
            play2=play2+1

print(play1)
print(play2)
