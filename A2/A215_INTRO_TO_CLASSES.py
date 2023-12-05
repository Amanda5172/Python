import sys
import math

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

def absolute_value(x):
    if x < 0:
        return -x
    return x


#Exercise 1
def turn_clockwise(dire):
    match dire:
        case "N":
            return "E"
        case "E":
            return "S"
        case "S":
            return "W"
        case "W":
            return "N"
        
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)


#Exercise 2
print()

def day_name(n):
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 0:
            return "Sunday"
        case _:
            return None

test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None)

#Exercise 3
print()

def day_num(n):
    match n:
        case "Monday":
            return 1
        case "Tuesday":
            return 2
        case "Wednesday":
            return 3
        case "Thursday":
            return 4
        case "Friday":
            return 5
        case "Saturday":
            return 6
        case "Sunday":
            return 0
        case _:
            return None

test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
test(day_num("Halloween") == None)

#Exercise 4
print()

def day_add(name,add):
    s=day_num(name)
    n=s+add
    while n>6:
        n=n-7
    return day_name(n)

test(day_add("Monday", 4) ==  "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")

#Exercise 5
print()

def day_add(name,add):
    s=day_num(name)
    n=s+add
    n=n%7
    return day_name(n)

test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")

#Exercise 6
print()

def days_in_month(name):
    match name:
        case "January"|"March"|"May"|"July"|"August"|"October"|"December":
            return 31
        case "February":
            return 28        
        case "April"|"June"|"September"|"November":
            return 30

test(days_in_month("February") == 28)
test(days_in_month("December") == 31)

#Exercise 7
print()

def to_secs(h,m,s):
    return 3600*h + 60*m +s

test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)

#Exercise 8
print()

def to_secs(h,m,s):
    return int(3600*h + 60*m +s)

test(to_secs(2.5, 0, 10.71) == 9010)
test(to_secs(2.433,0,0) == 8758)

#Exercise 9
print()

def hours_in(s):
    return int(s//3600)

def minutes_in(s):
    return int((s%3600)//60)

def seconds_in(s):
    return int((s%3600)%60)

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)

#Exercise 10
print()

test(3 % 4 == 0) #3
test(3 % 4 == 3)
test(3 / 4 == 0) #0.75
test(3 // 4 == 0)
test(3+4  *  2 == 14) #11
test(4-2+2 == 0) #4
test(len("hello, world!") == 13)

#Exercise 11
print()

def compare(n1,n2):
    n=n1-n2
    if n>0:
        return 1
    elif n==0:
        return 0
    else:
        return -1

test(compare(5, 4) == 1)
test(compare(7, 7) == 0)
test(compare(2, 3) == -1)
test(compare(42, 1) == 1)

#Exercise 12
print()

def hypotenuse(s1,s2):
    s=s1**2+s2**2
    return math.sqrt(s)

test(hypotenuse(3, 4) == 5.0)
test(hypotenuse(12, 5) == 13.0)
test(hypotenuse(24, 7) == 25.0)
test(hypotenuse(9, 12) == 15.0)
test(hypotenuse(8, 15) == 17.0)

#Exercise 13
print()

def slope(x1,y1,x2,y2):
    y=y2-y1
    x=x2-x1
    return y/x

test(slope(5, 3, 4, 2) == 1.0)
test(slope(1, 2, 3, 2) == 0.0)
test(slope(1, 2, 3, 3) == 0.5)
test(slope(2, 4, 1, 2) == 2.0)

def intercept(x1,y1,x2,y2):
    m=slope(x1,y1,x2,y2)
    c=y1-m*x1
    return c

test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)

#Exercise 14
print()

def is_even(n):
    if n%2==0:
        return True
    elif n%2==1:
        return False

test(is_even(2)==True)
test(is_even(1)==False)

#Exercise 15
print()

def is_odd(n):
    if n%2==0:
        return False
    elif n%2==1:
        return True

test(is_odd(2)==False)
test(is_odd(1)==True)

#Exercise 16
print()

def is_factor(f,n):
    if n%f==0:
        return True
    else:
        return False

test(is_factor(3, 12))
test(not is_factor(5, 12))
test(is_factor(7, 14))
test(not is_factor(7, 15))
test(is_factor(1, 15))
test(is_factor(15, 15))
test(not is_factor(25, 15))

#Exercise 17
print()

def is_multiple(m,n):
    return is_factor(n,m)

test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))

#Exercise 18
print()

def f2c(t):
    c=((t-32)*5)/9
    return round(c)

test(f2c(212) == 100)     # Boiling point of water
test(f2c(32) == 0)        # Freezing point of water
test(f2c(-40) == -40)     # Wow, what an interesting case!
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)

#Exercise 19
print()

def c2f(t):
    c=(9*t)/5+32
    return round(c)

test(c2f(0) == 32)
test(c2f(100) == 212)
test(c2f(-40) == -40)
test(c2f(12) == 54)
test(c2f(18) == 64)
test(c2f(-48) == -54)
