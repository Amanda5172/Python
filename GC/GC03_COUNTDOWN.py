import time

t= int(input("Length of countdown in seconds: "))

for i in range(t):
    print("T-minus",t-i,"and counting")
    time.sleep(1)

print("Lift-off!")
