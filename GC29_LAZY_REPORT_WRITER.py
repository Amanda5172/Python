import random


r1 =" should elaborate more."

r2 = " needs to write more points."

r3 = " has shown an enthusiastic approach to all aspects of the course."

r4 = " has made excellent progress."

r5 = " is very conscientious and shows excellent effort and care with daily work."

r6 = " continues to hand in superb Economics assignments."

r7 = ", well done!"

r8 = " has many insightful ideas to share with the class."

r9 = " has improved steadily."

r10 = " has made good academic progress this term."

r11 = " exhibits a positive attitude in the classroom and shows enthusiasm for classroom activities."

r12 = ", keep up the good work!"

r13 = " has room for improvement in the quality of work."

r14 = " should submit more practice questions for feedback to see more improvement."

r15 = " has shown good work ethics and has successfully fulfilled all the learning objectives."

r16 = " is well mannered and participates fairly well in class discussion and activities."



r = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16]#,r17,r18,r19,r20]

n = random.randint(0,15)

name = str(input("Student name: "))

print(name+r[n])
