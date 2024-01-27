
student_names = [{"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
              {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
              {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}, ]

def get_selection():
    get_student = {}
    get_student["name"] = input("Please enter the student name: ")
    get_student["hometown"] = input("Please enter the student hometown: ")
    get_student["favorite food"] = input("Please enter the student favorite food: ")
    return get_student

def list_names(names):
    for student in names:
        names.index(student) +1, student['name']

        list_names(student_names)


while True:
    user_input = input("Please select which action you'd like to do: add, view, or quit? ")
    if user_input == 'add':
          get_student = get_selection()
          list_names.append(student_names)
          print(list_names)
    # elif user_input == 'view':





    #     if 0 <= greeting - 1 < len(names):
    #      print(f"Student {names[greeting - 1]}. What would you like to know about this student?")
    #      response = input('Enter "hometown" or "favorite food": ')
    #      if response == "hometown":
    #          print(f"{names[greeting - 1]}'s hometown is {home_town[greeting - 1]}.")
    #     elif response == "favorite food":
    #         print(f"{names[greeting - 1]}'s favorite food is {favorite_food[greeting - 1]}.")
    #     else:
    #          print("Invalid response. Please try again.")
    #
    # elif user_input == 'quit':
    #     print("Good bye")
    #     break
    # else:
    #     print("Invalid statement. Please tray again.")









# go_on = 'y'

# while True:
# student_option = "notstarted"

# while(not student_option.isdigit()\
#         or not(int(student_option) >0\
#         and int(student_option) <= len(list_names))):
#     print(f"Please select which action you'd like to do: add, view, or quit? ")
#     student_option = input("> ")



#
# while True:
#     try:
#         greeting = int(input("Welcome! Which student would you like to learn more about? Enter a number 1-4 (Enter 0 to exit): "))
#         if greeting == 0:
#             break
#         students(names, home_town, favorite_food)
#     except ValueError:
#         print("Invalid entry. Please enter a valid number.")