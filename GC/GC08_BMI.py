weight = float(input("Weight in kilograms: "))
height = float(input("Height in metres: "))

bmi = weight / (height**2)

print(bmi)


if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<25:
    print("Normal weight")
elif 25<=bmi<30:
    print("Obese")

