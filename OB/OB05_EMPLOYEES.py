class employees:
    def __init__(self):
        self.__firstname=""
        self.__lastname=""
        self.__fullname=""
        self.email=""
        self.employeeid=""
    def constructor(self,firstname,lastname):
        self.__fullname=firstname+' '+lastname
        mail=firstname+'.'+lastname+'@company.com'
        self.__email=mail.lower()
    def printdetails(employeeid):
        print("First name:",self.__firstname)
        print("Last name:",self.__lastname)
        print("Full name:",self.__fullname)
        print("Email:",self.__email)
        print("Employee ID:",self.__employeeid)

