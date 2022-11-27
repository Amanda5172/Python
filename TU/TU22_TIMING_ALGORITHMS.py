import datetime

print("Measure your typing time.")
start_time = datetime.datetime.now()
u = input("Type 'the lazy fox jumped over the brown dog': ")
time_taken = datetime.datetime.now()-start_time  
print(time_taken)
