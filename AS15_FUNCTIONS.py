def hello1():
    print('Hello World')
 
def add1(x, y):
    print(f'arguments are {x} and {y}')
    return x + y

hello1()
sum = add1(10, 5)
print(f'sum is {sum}')


print()


def hello(year=2019):
    print(f'Hello World {year}')
 
hello(2020)
hello()


print()


def odd_even_checker(i):
    if i % 2 == 0:
        return 'even'
    else:
        return 'odd'
 
print(odd_even_checker(2))
print(odd_even_checker(5))


print()


def return_odd_ints(i):
    x = 1
    while x <= i:
        yield x
        x += 2
 
output = return_odd_ints(10)
for out in output:
    print(out)

def add(x, y, *args, **kwargs):
    sum = x + y
    for a in args:
        sum += a
 
    for k, v in kwargs.items():
        sum += v
    return sum
 

total = add(1, 2, *(3, 4), **{"k1": 5, "k2": 6})
print(total) 


print()


def fibonacci_numbers_at_index(count):
    if count <= 1:
        return count
    else:
        return fibonacci_numbers_at_index(count - 1) + fibonacci_numbers_at_index(count - 2)
 
count = 7
i = 1
while i <= count:
    print(fibonacci_numbers_at_index(i))
    i += 1


print()


class Data:
    def foo(self):
        print('foo method')
 
 
def foo():
    print('foo function')
 
foo()
 
d = Data()
d.foo()
 
print(type(foo))
print(type(d.foo))


print()


def square(x):
    return x * x
 
f_square = lambda x: x * 3
 
print(square(10))  
print(f_square(10))  
