from hotel_room import Room
from hotel_room import room_type

print ("Welcome to our Hotel booking!")

def create_menu():
    print("Enter 1 to view user information")
    print("Enter 2 to view available rooms")
    print("Enter 3 to view current booking")
    print("Enter 4 to view receipt")
    print("Enter 5 to exit")
    choice = input("Enter your selection:")
    return choice

user_choice = ""
print(user_choice)

while user_choice != "5":
    user_choice = create_menu()
    
    if (user_choice == "1"):
        print("Add user_info")
    elif (user_choice == "2"):
        print(room_type)
    elif (user_choice == "3"):
        print("current booking")
    elif (user_choice == "4"):
        print("receipt")
    elif (user_choice == "5"):
        continue
    else: 
        print("Invalid input")
    
    input("press enter to continue....")


print("Thank you for using the booking app")
