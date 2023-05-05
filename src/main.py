# import modules & packages
from hotel_room import Room
from hotel_room import room_type
from hotel_room import room
from user import get_user

# Welcome message
print ("Welcome to our Hotel booking!")

# making a booking 
booking = "booking_records.csv"
user_info = get_user()
current_booking = {"user_info": user_info, "room_type": room_type}

# main menu 
def create_menu():
    print("Enter 1 to view user information")
    print("Enter 2 to view available rooms")
    print("Enter 3 to make a new booking")
    print("Enter 4 to view past booking")
    print("Enter 5 to exit")
    choice = input("Enter your selection:")
    return choice

user_choice = ""
print(user_choice)

# main menu loop and choices
while user_choice != "5":
    user_choice = create_menu()
    
    if (user_choice == "1"):
        print(user_info)
    elif (user_choice == "2"):
        print(room_type)
        user_input = input('Would you like to make a new booking Y or N?: ')
        if user_input == 'Y':
            print (new_booking)
        elif user_input == 'N':
            print ("Thank you for browsing! We will take you back to the main menu")
            continue
        else: 
            print("Invalid input")
    elif (user_choice == "3"):
        print(user_info, room_type)
    elif (user_choice == "4"):
        print("receipt")
    elif (user_choice == "5"):
        continue
    else: 
        print("Invalid input")
    
    input("press enter to continue....")


print("Thank you for using the Hotel booking app")
