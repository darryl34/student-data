nameAndEmail = []
count = int(input("How many students are there in this class? "))

for i in range(count):
    name = str(input("Student Name: "))
    email = str(input("Student's Email Address: "))
    dob = str(input("Student's Date of Birth: "))
    std_id = str(input("Student's ID: "))
    newStudent = [name, email, dob, std_id]
    nameAndEmail.append(newStudent)
print()
dash = '-' *80

print('{:^20}{:^30}{:^15}{:^15}'.format("STUDENT NAME", "STUDENT EMAIL ADDRESS", "STUDENT DOB", "STUDENT ID"))
print(dash)
for i in range(count):
    data = nameAndEmail[i]
    print('{:^20}{:^30}{:^15}{:^15}'.format(data[0], data[1], data[2], data[3]))

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

namePrompt = str(input("Please input a student's name: "))
for i in range(count):
    data = nameAndEmail[i]
    if namePrompt in data[0]:
        print("Student Full Name: ",data[0])
        print("Student Email Address: ",data[1])
        print("Student Date of Birth: ",data[2])
        print("Student ID: ",data[3])
