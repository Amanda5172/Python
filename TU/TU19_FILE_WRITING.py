with open("counter.txt","w") as new_file:
    for i in range(10,-1,-1):
        line_to_write = str(i)+"\n"
        new_file.write(line_to_write)

