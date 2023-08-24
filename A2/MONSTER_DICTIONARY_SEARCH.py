dict = {}

with open("monsters_simple.txt","r") as ef:
  for line in ef:
    com = line.find(",")
    key = line[:com]
    value = line[com+1:-1]
    dict[key]=value

#print(dict)

inp = input("Name of monster: ")

if dict.get(inp):
  print(dict[inp])
else:
  print("Not in dictionary.")

#https://gist.github.com/jamesabela/c36bbbc8a950470c35cb80a91da38278
