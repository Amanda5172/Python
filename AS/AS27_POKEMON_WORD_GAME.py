def connect(word):
    t = len(word)
    word[t-1]

def find(names,letter,count):
    global nums

    
    for i in names:
        if i[0]==letter:
            count=count+1
            names.remove(i)
            #print(i,count)
            find(names,i[-1].upper(),count)
            names.append(i)
            count=count-1
            
    #input(count)
    if count>nums[0]:
        nums[0] =count
    
    return 


names=[]
with open("names.txt","r") as ef:
    for line in ef:
        names.append(line.strip("\n"))

    
nums=[0]
find(names, "B",0)
print(nums)
