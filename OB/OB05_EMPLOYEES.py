class employee:
    def __init__(self):
        self.__employeeid=""
        self.__firstname=""
        self.__lastname=""
        self.__fullname=""
        self.__email=""
    def constructor(self,firstname,lastname):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__fullname=firstname+' '+lastname
        mail=firstname+'.'+lastname+'@company.com'
        self.__email=mail.lower()
    def getemployeeemail(self,employeeid):
        return self.__email
    def printdetails(self,employeeid):
        print("Employee ID:",self.__employeeid)
        print("First name:",self.__firstname)
        print("Last name:",self.__lastname)
        print("Full name:",self.__fullname)
        print("Email:",self.__email)
        

p=[]
with open("emailList.txt","r") as ef:
    for line in ef:
        p.append(line.strip("\n"))

employees =[]
for i in range(0,int(len(p)/2),2):
    t = employee()
    t.constructor(p[i],p[i+1])
    employees.append(t)


print(employees[2].getemployeeemail("2"))
employees[2].printdetails("2")
