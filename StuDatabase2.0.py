#  dictionary list
student_names = [{"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
                 {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
                 {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}, ]


# def function to add onto student_names list in while true/if loop
def get_new_student():
    new_student = {}
    new_student["name"] = input("Please enter the student first name:> ")
    new_student["hometown"] = input("Please enter the student hometown:> ")
    new_student["favorite food"] = input("Please enter the student favorite food:> ")
    return new_student


# def function to print student names in while true/elif loop
def print_student_names(names):
    for student in names:
        print(names.index(student) + 1, student['name'])


while True:  # will repeat everything in this loop depending on operational choices
    print("Welcome to the Student Database Version2.0\n")
    user_input = input('Please select which action you would like to take: "add", "view", or "quit"?\n>')
    if user_input == 'add':  # if section for def function get_new_student() to add on new student information
        new_student = get_new_student()
        student_names.append(new_student)
        print(f"Update Successful!\n{new_student}")
    elif user_input == 'view':  # elif section for def funct print_student_names to show list of student names from dict list student_names.
        print_student_names(student_names)
    elif user_input == 'quit':
        print("GOOD BYE!")
        break
    else:
        print("Invalid statement. Please tray again.\n")
