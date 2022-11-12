count = 1
while True:
    MyNumber = input("Please enter a number: ")
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \nI asked for a number...")
    count = count + 1
print(valid_number)
print("It took you", count, "number of tries!")

