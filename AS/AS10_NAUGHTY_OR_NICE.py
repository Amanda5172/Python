#It contains at least three vowels (aeiou only)
#It contains at least one letter that appears twice in a row
#It does not contain the strings ab, cd, pq, or xy,
c=0

def nicecheck(line):
    Nice=False
    vowels=0
    dl=0
    dss=0
    for i in range(0,len(line)-1):
        #line[i]
        if line[i] in ['a','e','i','o','u']:
            vowels=vowels+1
        if line[i]==line[i+1]:
            dl=dl+1
        ss=str(line[i]+line[i+1])
        if ss in ['ab', 'cd', 'pq', 'xy']:
            dss=dss+1
    if vowels>2 and dl>0 and dss==0:
        return True
#I put the list of strings into 'non.txt'
with open("non.txt","r") as ef:
    for line in ef:
        if nicecheck(line)==True:
            c=c+1

print(c)
