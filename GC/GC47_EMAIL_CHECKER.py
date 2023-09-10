import string

list1 = [0,1,2,3,4,5,6,7,8,9,"!","#","$","%","&","'","*","+","-","/","=","?","^","_","`","{","|","}","~"]
list2 = [0,1,2,3,4,5,6,7,8,9,"-","."]

for i in list(string.ascii_letters):
    list1.append(i)
    list2.append(i)

#print(list1)
#print(list2)


check = input("Enter your email address: ")

at = check.find("@")
c1 = check[:at]
c2 = check[at+1::]

ch1 = True
ch2 = True


for r in c1:
    if r not in list1:
        ch1 = False
for t in c2:
    if t not in list2:
        chp2 = False

if ch1==False or ch2==False or at==-1:
    print("Invalid email.")
else:
    print("Valid email.")
