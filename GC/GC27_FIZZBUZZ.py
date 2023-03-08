a=int(input())
for i in range(1,a+1):
    if i%15==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
