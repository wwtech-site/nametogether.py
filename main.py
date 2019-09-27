import random

stud1 = ["student3", "student2", "student1"]
puffer = []
prog = 0

while prog!=len(stud1):
    randint = random.randint(0, len(stud1)-1)

    if stud1[prog] ==stud1[randint] or stud1[randint] in puffer:
        pass
    else:
        print(stud1[prog] + " wird " + stud1[randint] + "'s ehre nehmen.")
        puffer.append(stud1[randint])
        prog = prog+1