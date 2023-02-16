length=float(input("input the length: "))

gr = (1 + 5**(1/2))/2

width=gr*length

print("width:",width)

#check
x=round(width/length,10)
y=round(length/(width-length),10)
if x==y:
    print("check passed")
