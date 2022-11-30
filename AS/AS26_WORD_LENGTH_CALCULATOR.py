import string
y=0
#y is total word length
wc=0
#wc is word count

with open("helloworld.txt", "r") as ef:
    for line in ef:
        s = line.translate(str.maketrans('','',string.punctuation))
        x=s.split()
        for t in range(len(x)):
            if x[t] !="":
                y=y+len(x[t])
                wc=wc+1
        

print("Average word length:",y/wc)

