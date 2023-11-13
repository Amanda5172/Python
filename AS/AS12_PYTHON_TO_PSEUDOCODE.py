import string
import re

changelist = { "=":"←","==":"←","if":"IF","for":"FOR","while":"WHILE","else":"ELSE","elif":"ELIF","def":"FUNCTION", "print":"OUTPUT", "return":"RETURN","input":"INPUT"}

def pseudo(line):
    line = re.split(r'(\s+)', line)
    for key, value in changelist.items():
        for word in line:
            if key == str(word):
                line[line.index(word)] = value
        #for key, value in advanced_conversion_rules.items():
            #for word in line:
           #     line[line.index(word)] = word.replace(key, value)
      
    f = "".join(line)
    return f

#print(pseudo("def test_suite(): test(absolute_value(17) == 17)"))

with open("challenge 2.py","r") as ef:
    with open("write.txt","w") as wr:
        for line in ef:
            l= line.strip("\n")
            f = pseudo(l)
            wr.write(f)
            wr.write("\n")
            
