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

def delStudent():
    delStudent = str(input("Do you wish to delete any students? (y/n) "))
    if delStudent == "y":
        print(nameAndEmail)
        print()
        value = int(input("Which value would you like to delete? (Enter a number) "))
        value -= 1
        print()
        print("Updated student data: ")
        del nameAndEmail[value]
        for i in nameAndEmail:
            print(i)
    else:
        return

delStudent()
