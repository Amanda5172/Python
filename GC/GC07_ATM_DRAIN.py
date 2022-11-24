to = 100.40
print("You have $100.40 in your account.")
x = float(input("How much do you want to withdraw? "))

w=1.5 * x


if x%5 == 0 and to>w:
    print("Withdrawal successful.")
    nt = to - w
    r = str(nt)
    tt = r.find(".")
    rt = r[0:tt+3]
    print("You have $%s in your account." % rt)
    
else: 
  print("Withdrawal invalid.")
