from datetime import datetime

a = str(input("Start date(eg. Jun 1 2005): "))
b = str(input("End date(eg. Aug 1 2005): "))
#date must be written in format month day year, eg. Jun 1 2005


start = datetime.strptime(a,'%b %d %Y')
end = datetime.strptime(b,'%b %d %Y') 

print(end-start)

