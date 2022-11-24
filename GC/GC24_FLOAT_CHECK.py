r = input("Input a float number: ")

try:
    float(r)
except ValueError:
    print("Not a float")
