nameAndEmail = []
count = int(input("How many students are there in this class? "))

for i in range(count):
    name = str(input("Student Name: "))
    email = str(input("Student's Email Address: "))
    newString = name + "#" + email
    nameAndEmail.append(newString)
print()
dash = '-' *50

print('{:^20}{:^30}'.format("STUDENT NAME", "STUDENT EMAIL ADDRESS"))
print(dash)
for i in range(count):
    data = nameAndEmail[i].split('#')
    print('{:^20}{:^30}'.format(data[0], data[1]))
