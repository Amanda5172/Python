with open("counter.txt","r") as whole_file:
    for line in whole_file:
        t = int(line)


with open("counter.txt","a") as existing_file:
    for i in range(t,t+11):
        w = str(i)+"\n"
        existing_file.write(w)

